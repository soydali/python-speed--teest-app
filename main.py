from tkinter import *
from tkinter import font
from PIL import Image
from PIL import ImageTk
import speedtest


root = Tk()


w = 700
h = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

root.geometry("%dx%d+%d+%d" % (w,h,x,y))

root.title("Speed Test By Soleus")
root.resizable(False,False)
root.config(bg="#272742")
root.iconbitmap("media/wifi-icons.ico")





def run_check():
    root.update()
    test = speedtest.Speedtest(secure=True)

    Uploading = round(test.upload() / (1024 * 1024), 2)
    upload_label.config(text="UPLOAD: " + str(Uploading))

    Downloading = round(test.download() / (1024 * 1024), 2)
    download_label.config(text="DOWNLOAD: " + str(Downloading))

    servernames = []
    test.get_servers(servernames)
    ping_label.config(text="PING: " + str(test.results.ping))


def Check():

    calisiyor_label = Label(root, text="ÇALIŞIYOR LÜTFEN BEKLEYİN...", bg="#272742", font="arial 15 bold",height=700, width=700)
    calisiyor_label.pack()

    root.update()
    run_check()

    calisiyor_label.destroy()


#RESİMLER

start_button = ImageTk.PhotoImage(file="media/start-button.png")
speed_top = ImageTk.PhotoImage(file="media/bg.png")

#ETİKETLER

Label(root,image=speed_top,border="0px").pack(pady=(80,0),padx=(0,30))   
Button = Button(root,image=start_button,bg="#272742",activebackground="#272742",border=0,command=Check).pack(pady=(40,0),padx=(0,35))

#PİNG DOWNLOAD UPLOAD
download_label =Label(root,text="DOWNLOAD",font="arial 15 bold",bg="#272742")
download_label.place(x=50,y=542)

upload_label = Label(root,text="UPLOAD",font="arial 15 bold",bg="#272742")
upload_label.place(x=290,y=542)


ping_label = Label(root,text="PING",font="arial 15 bold",bg="#272742")
ping_label.place(x=550,y=542)


#CREATED BY SOLEUS
ozel_font = font.Font(family="Century", size="12")
created_label = Label(root,text="Created By Soleus",font=ozel_font,bg="#272742").pack(anchor=SE,pady=(210,0),padx=(0,15))



root.mainloop()
