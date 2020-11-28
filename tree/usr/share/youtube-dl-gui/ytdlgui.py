#!/usr/bin/env python3

infos = {"author": "TheTechRobo", "license": "GPLv3", "type": "gui", "category": "internet", "category2": "video", "category3": "python"}

from tkinter import Button, Tk, Entry, Toplevel, PhotoImage, Label
from tkinter import messagebox as mbox
from subprocess import Popen
from sys import stdout as sstdout

window = Tk()

mbox.showinfo("Copyright","Copyleft (c) 2020 TheTechRobo. Licensed under the GPLv3.")
mbox.showinfo("Copyright","You should have received a copy with this Software. Else, go to http://raw.githubusercontent.com/thetechrobo/youtube-dl-gui/master/LICENSE")
def commence():
    mbox.showinfo("...","Commencing download...")
    url = Widgets.video.get()
    load = Toplevel(window)
    image = PhotoImage(file='/usr/share/youtube-dl-gui/pleasewait.png')
    Label(load, image=image).pack()
    try:
        hi = Popen(["youtube-dl", url], shell=False, stdout=sstdout, stderr=sstdout)
    except Exception as ename:
        mbox.showerror("ERROR!", "An error occured.")
        print(ename)
    else:
        print(hi.communicate())

class Widgets:
    video = Entry(window)
    text = Label(text="Please insert a URL.")

Widgets.text.pack()
Widgets.video.pack()
Button(window, text="OK", command=commence).pack()

window.mainloop()
