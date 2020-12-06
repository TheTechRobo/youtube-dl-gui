#!/usr/bin/env python3

infos = {"author": "TheTechRobo", "license": "GPLv3", "type": "gui", "category": "internet", "category2": "video", "category3": "python"}

from tkinter import Button, Tk, Entry, Toplevel, PhotoImage, Label, Frame, YES#, BOTH
from tkinter import messagebox as mbox
from subprocess import Popen
from sys import stdout as sstdout
from playsound import playsound
import sys
sys.dont_write_bytecode = True

window = Tk()

def getPhoto(window): 
    """
    This is not necessary anymore but im too lazy to move it out lol
    """
    image = PhotoImage(file='/usr/share/youtube-dl-gui/pleasewait.png')
    Label(window, image=image).pack(fill="both", expand=False, side="top")
    return image

mbox.showinfo("Copyright","Copyleft (c) 2020 TheTechRobo. Licensed under the GPLv3.")
mbox.showinfo("Copyright","You should have received a copy with this Software. Else, go to http://raw.githubusercontent.com/thetechrobo/youtube-dl-gui/master/LICENSE")
def commence():
    global photo #This is necessary because https://stackoverflow.com/a/16424553/9654083
    #AKA, It prevents the image from getting garbage collected
    mbox.showinfo("Commencing download...","Press OK to start...")
    url = Widgets.video.get()
    if url == "":
        mbox.showerror("Error", "Next time please type a URL.")
    load = Toplevel(window)
    load.geometry("1000x1000")
    photo = getPhoto(load)
    termf = Frame(load, height=50, width=200)
    termf.pack(side="bottom", fill="both", expand=YES) #https://stackoverflow.com/questions/37017472/python-tkinter-place-put-frame-to-the-bottom
    wid = termf.winfo_id()
    try:
        Popen(['xterm -into %d -geometry 200x50 -sb -e /bin/sh -c "youtube-dl %s;sleep 1;exit"' % (wid, url)], stdout=sstdout, stderr=sstdout, shell=True)
    except Exception as ename:
        mbox.showerror("ERROR!", "An error occured.")
        print(ename)

class Widgets:
    video = Entry(window)
    text = Label(text="Please insert a URL.")

Widgets.text.pack()
Widgets.video.pack()
Button(window, text="OK", command=commence).pack()

playsound("/usr/share/youtube-dl-gui/loading_music.mp3")

window.mainloop()
