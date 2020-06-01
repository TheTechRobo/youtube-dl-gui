infos = {"author": "TheTechRobo", "license": "GPLv3", "type": "gui", "category": "internet", "category2": "video", "category3": "python"}

from tkinter import Button, Tk, Entry
from tkinter import messagebox as mbox
from subprocess import Popen, PIPE

window = Tk()

def commence():
    mbox.showinfo("...","Commencing download...")
    url = Widgets.video.get()
    try:
        hi = Popen(["youtube-dl", url], shell=False, stdout=PIPE, stderr=PIPE)
    except:
        mbox.showerror("ERROR!", "yt-downloader does not look installed")
    else:
        print(hi.communicate())

class Widgets:
    video = Entry(window)
    Button(window, text="OK", command=commence).pack()

Widgets.video.pack()

window.mainloop()
