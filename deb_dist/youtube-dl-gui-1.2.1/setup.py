import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "youtube-dl-gui",
    version = "1.2.1",
    author = "TheTechRobo",
    description = "Frontend for youtube-dl",
    license = "GPLv2",
    url = "https://github.com/thetechrobo/youtube-dl-gui",
    packages=['youtube-dl-gui'],
    #entry_points = {
        #'console_scripts' : ['youtube-dl-gui = myscript.myscript:main']
    #},
    data_files = [
        ('tree/usr/share/applications/', ['youtube-dl-gui.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
