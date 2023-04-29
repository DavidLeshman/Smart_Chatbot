from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os


root=Tk()
root.title('Music player project by TechVidvan')
root.geometry("920x670+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(False, False)
mixer.init()


def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdire(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
 
def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


Icon_Image = PhotoImage(file="C:/1/musiclogo.jpg")
root.iconphoto(False,Icon_Image = PhotoImage(file="musiclogo.jpg"))
 
Top_Image = PhotoImage(file="musiclogo.jpg")
Label(root, image=Top_Image, bg="#0f1a2b").pack()
 
#logo
logo_Image = PhotoImage(file="musiclogo.jpg")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=65, y=115)


Button_Play = PhotoImage(file="play.jpeg")
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=100, y=400)
 
Button_Stop = PhotoImage(file="stop.png")
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)
 
Button_Resume = PhotoImage(file="resume.png")
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)
 
Button_Pause = PhotoImage(file="pause.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)
 
#music
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)
 
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=330, y=300)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()

