infos = {"author": "TheTechRobo", "license": "GPLv3", "type": "gui", "category": "internet", "category2": "video", "category3": "python"}

from tkinter import Button, Tk, Entry
from tkinter import messagebox as mbox
from subprocess import Popen
from sys import stdout as sstdout

window = Tk()

mbox.showinfo("Copyright","Copyleft (c) 2020 TheTechRobo. Licensed under the GPLv3.")
mbox.showinfo("Copyright","You should have received a copy with this Software. Else, go to http://raw.githubusercontent.com/thetechrobo/youtube-dl-gui/master/LICENSE")
def commence():
    mbox.showinfo("...","Commencing download...")
    url = Widgets.video.get()
    try:
        hi = Popen(["youtube-dl", url], shell=False, stdout=sstdout, stderr=sstdout)
    except:
        mbox.showerror("ERROR!", "youtube-dl does not look installed")
    else:
        print(hi.communicate())

class Widgets:
    video = Entry(window)
    Button(window, text="OK", command=commence).pack()

Widgets.video.pack()

window.mainloop()
