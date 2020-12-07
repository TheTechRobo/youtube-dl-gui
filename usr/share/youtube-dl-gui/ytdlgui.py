#!/usr/bin/env python3

infos = {"author": "TheTechRobo", "license": "GPLv3", "type": "gui", "category": "internet", "category2": "video", "category3": "python"}

moreCredits = ["https://stackoverflow.com/questions/17760871/python-tkinter-photoimage", "https://stackoverflow.com/questions/15306631/how-do-i-create-child-windows-with-python-tkinter", "https://stackoverflow.com/a/31088999/9654083", "https://stackoverflow.com/a/7331836/9654083"]

from tkinter import Button, Tk, Entry, Toplevel, PhotoImage, Label, Frame, YES, IntVar, Checkbutton
from tkinter import messagebox as mbox
from subprocess import Popen
from sys import stdout as sstdout
from mpyg321 import MPyg321Player
import time
import threading

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

def musicbox(wid, url, load):
    global command
    if Variables.audioSelect.get():
        player = MPyg321Player()
        player.play_song("/usr/share/youtube-dl-gui/loading_music.mp3")
    command = Popen(['exec xterm -into %d -geometry 200x50 -sb -e /bin/sh -c "youtube-dl %s;sleep 1;exit"' % (wid, url)], stdout=sstdout, stderr=sstdout, shell=True)
    command.wait()
    player.stop()
    load.destroy()

def cancel():
    mbox.showinfo("Cancelling...", "NOTE : Cancelling may leave some temporary files in the current folder; they are safe to delete.\nPlease press OK to cancel...")
    command.terminate() #https://stackoverflow.com/a/13143013/9654083

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
    time.sleep(1)
    termf = Frame(load, height=50, width=200)
    termf.pack(side="bottom", fill="both", expand=YES) #https://stackoverflow.com/questions/37017472/python-tkinter-place-put-frame-to-the-bottom
    wid = termf.winfo_id()
    Label(load, text="Closing the window WILL NOT CANCEL THE PROCESS! To cancel it, click the button below. (If it doesn't work, click inside the white terminal frame, and type Ctrl and C at the same time.)").pack()
    Button(load, text="CANCEL PROCESS", command=cancel).pack()
    try:
        thread = threading.Thread(target=musicbox, daemon=True, args=(wid, url, load)) #https://realpython.com/intro-to-python-threading/
        thread.start()
    except Exception as ename:
        mbox.showerror("ERROR!", "An error occured.")
        print(ename)

class Variables:
    audioSelect = IntVar()
    audioSelect.set(1)

class Widgets:
    video = Entry(window)
    text = Label(text="Please insert a URL.")
    audio = Checkbutton(variable=Variables.audioSelect, onvalue=True, offvalue=False, text="Add loading music?") #https://stackoverflow.com/a/16285194/9654083

Widgets.text.pack()
Widgets.video.pack()
Widgets.audio.pack()
Button(window, text="OK", command=commence).pack()

window.mainloop()
