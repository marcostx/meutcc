import numpy as np
from glob import glob
from os.path import join, basename, splitext, isdir
import os


all_classes = []
all_videos  = []

EXTENSIONS = [ "png" ]

datasetpath = 'UCF-101'
    
# Getting each class name
for cl in glob(datasetpath + "/*"):
	all_classes.extend([join(datasetpath, basename(cl))])

for i in xrange(len(all_classes)):
    for vid in glob(all_classes[i] + "/*"):
        all_videos.extend([join(all_classes[i], basename(vid))])

for i in xrange(len(all_videos)):
    if all_videos[i].split('.')[1] in EXTENSIONS:
    	# remove . 
    	print all_videos[i]
    	cmd = "rm -rf " + all_videos[i]
    	os.system(cmd)
	
        

#for idx, vid in enumerate(all_videos):
#    print("Analysing video ", vid )
