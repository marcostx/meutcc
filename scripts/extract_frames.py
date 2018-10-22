from glob import glob
import os
from os.path import basename, join, exists

targetFolder = "frames"
all_classes = []
all_videos = []

# getting the classes
for cl in glob(targetFolder + "/*"):
    all_classes.extend([join(targetFolder, basename(cl))])

for i in xrange(len(all_classes)):
    for vid in glob(all_classes[i] + "/*"):
        all_videos.append(vid)

for vid in all_videos:
    cl = vid.split("/")[-2]
    video = basename(vid).split(".")[0]

    # creating a folder to store the frames of the video
    if not exists("frames/" + cl + "/" + video):
        os.mkdir("frames/" + cl + "/" + video)

        # Taking the frames ..
        cmnd = "ffmpeg -i "+ vid +" -vf fps=30 frames/" + cl + "/"+ video + "/"+ video +".%04d.jpg"
        os.system(cmnd)

## end