"""

//[]------------------------------------------------------------------------[]
//|                                                                          |
//|                         Video Processing Module                          |
//|                               Version 1.0                                |
//|                                                                          |
//|              Copyright 2015-2020, Marcos Vinicius Teixeira               |
//|                          All Rights Reserved.                            |
//|                                                                          |
//[]------------------------------------------------------------------------[]
//
//  OVERVIEW: process_video.py
//  ========
//  Source file for process an input video and get the frames. The task is trasform 
//  a video into a sequence of frames and save them in a folder appropriate.
//  


// Parameters:
// sys.args[1] => class of the video
// sys.args[2] => name of the video

"""



FOLDER = 'frames'

def doc():
 	print (__doc__)

import os
import numpy as np
import cv2
import time
import sys
from os import mkdir
from os.path import splitext, exists

if len(sys.argv) < 2:
	print"Usage: ./process_video video_path"
	exit(1)


# getting the name of video
vname = sys.argv[1]

# Reading the video
print " Processing " + vname + " ... "

if not exists(FOLDER):
    mkdir(FOLDER)

cmd = "ffmpeg -i "+ vname +" -vf fps=1/1 "+ FOLDER +"/img%03d.jpg"
os.system(cmd)

