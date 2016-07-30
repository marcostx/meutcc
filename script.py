from glob import glob
import os
from os.path import basename, join, exists
from random import shuffle

targetFolder = "statefarm"
all_videos = []
train_videos = []
test_videos = []
train_frames = []
test_frames = []


aux_=[]
train_items_videos=[]


# getting the classes
for vid in glob(targetFolder + "/*"):
    all_videos.append(vid)

for i in xrange(len(all_videos[:2])):
   train_videos.append(all_videos[i])
   test_videos.append(all_videos[i])

for i in train_videos:
    for p in glob(i + "/*"):
        train_frames.append(p)

for i in test_videos:
    for p in glob(i + "/*"):
        test_frames.append(p)

# get class values
classes = {"c0":0,"c1":1}

shuffle(test_frames)
shuffle(train_frames)

f = open("newstateFarm_train.txt", "w")

train_values = []
train_lines=[]
test_lines=[]

for value in train_frames:
    v_ = value.split("/")[1:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[1].split("_")[1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    print(str_)
    train_lines.append(str_)

f.writelines(train_lines)
    
## end