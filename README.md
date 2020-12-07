# youtube-dl-gui
A small GUI frontend for youtube-dl

# Requirements
This has only been tested on Debian/Elive Linux, and will NEVER work on Windows unless there is  some major refactoring or you use Git Bash.

You will need the following package  `mpg321` and also `python3-tkinter`. 

# Credits
## Code
See inside of source code, there's stuff scattered around.
## Song
Pandemic by CHRISRGMFB  
https://chrisrgmfb.com  
Promoted by Royalty Free Planet: https://royaltyfreeplanet.com  
Creative Commons Attribution 3.0

# Instructions
There's three ways

## Installing the .deb (debian)
Go to this link. https://gofile.io/d/TGx4oA Install the deb file.

## Building a .deb file from source
Clone this repository, don't change into the directory, then type `dpkg-deb youtube-dl-gui`. There will be a resulting `youtube-dl-gui.deb`.

## Manual
Copy the files inside `usr` into your `/usr/` folder. Making sure it doesn't overwrite anything.
