import numpy as np
from glob import glob
from os.path import join, basename, splitext, isdir
import os


all_frames = []
all_videos  = []

EXTENSIONS = [ "png" ]

datasetpath = 'frames'
    
# Getting each video name
for cl in glob(datasetpath + "/*"):
	all_videos.extend([join(datasetpath, basename(cl))])

for i in xrange(len(all_videos)):
    for vid in glob(all_videos[i] + "/*"):
    	newf = vid.split("/")[1]+ "." + basename(vid).split(".")[1] + "." + basename(vid).split(".")[2]

    	os.rename(vid,join(all_videos[i], newf))
        #all_frames.extend([join(all_videos[i], newf)])

#for idx, vid in enumerate(all_videos):
#    print("Analysing video ", vid )
