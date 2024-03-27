import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="",text_color="white")
        video.download()
        finishLabel.configure(text = "download completed!!!",text_color="blue")
        print("success")

    except:
        finishLabel.configure(text="invalid youtube link",text_color="red")  
        print("eror")  

    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    ppercentage.configure(text = per + "%")
    print(per)
    ppercentage.update()

    progressBar.set(float(percentage_of_completion)/100)


#image

my_image = customtkinter.CTkImage(light_image=Image.open('images/1.jpg'),dark_image=Image.open('images/1.jpg'))
img = customtkinter.CTkLabel(app, text="", image = my_image)
img.pack(pady=10,padx=10)


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#our app frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("youtube downlaoder")


#my name
name = customtkinter.CTkLabel(app, text = "brought to you by christo joseph")
name.pack(padx =0, pady = 10)

#adding ui elements
title = customtkinter.CTkLabel(app, text="insert youtube link")
title.pack(padx=10, pady=10)




# link unput
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=40,textvariable=url_var)
link.pack()


#finished downloading

finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack(padx =10, pady=10)


#progreess %
ppercentage = customtkinter.CTkLabel(app, text="0%")
ppercentage.pack(padx =5,pady=10)

progressBar = customtkinter.CTkProgressBar(app, width = 400 )
progressBar.set(0)
progressBar.pack(padx=10,pady=5)




# dowbload b uttob

downlaod = customtkinter.CTkButton(app, text="downlaod", command=startDownload)
downlaod.pack(padx = 15, pady = 20)

# run app loop
app.mainloop()
