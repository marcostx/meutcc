from glob import glob
import os
from os.path import basename, join, exists

targetFolder = "ucf_sports_actions"
all_classes = []
all_videos = []

# getting the classes
for cl in glob(targetFolder + "/*"):
    all_classes.extend([join(targetFolder, basename(cl))])

for i in xrange(len(all_classes)):
    count=0
    for vid in glob(all_classes[i] + "/*"):
    	filename = vid.split("/")[-1].split(".")[0]
    	type_ = vid.split("/")[-1].split(".")[2]
        number = vid.split("/")[-1].split(".")[1]
    	new_name = ("frame." + number + "." + type_)
        new_path = targetFolder + "/" + vid.split('/')[1] + "/" + new_name

            os.rename(vid, new_path)
    	count+=1
       	

