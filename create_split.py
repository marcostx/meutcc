from glob import glob
import os
from os.path import basename, join, exists
from random import shuffle

targetFolder = "ucf_sports_actions"
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

for i in xrange(len(all_videos)):
    for idx, vid in enumerate(glob(all_videos[i] + "/*")):
        if idx < ((len(glob(all_videos[i] + "/*"))*70)/100):
            train_videos.append(vid)
        else:
            test_videos.append(vid)

for i in train_videos:
    for p in glob(i + "/*"):
        train_frames.append(p)

for i in test_videos:
    for p in glob(i + "/*"):
        test_frames.append(p)

# get class values
classes = {"Diving-Side":0,"Golf-Swing-Front":1,"Golf-Swing-Side":2,"Kicking-Front":3,
"Kicking-Side":4,"Lifting":5,"Riding-Horse":6,"Run-Side":7,
"SkateBoarding-Front":8,"Swing-Bench":9,"Swing-SideAngle":10,"Walk-Front":11}

shuffle(test_frames)
shuffle(train_frames)

f = open("ucf12_split_train_videos.txt", "w")
g = open("ucf12_split_test_videos.txt", "w")
train_values = []
train_lines=[]
test_lines=[]

for value in train_frames:
    v_ = value.split("/")[2:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[2].split("0")[0][0:-1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    train_lines.append(str_)

for value in test_frames:
    v_ = value.split("/")[2:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[2].split("0")[0][0:-1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    test_lines.append(str_)

f.writelines(train_lines)
g.writelines(test_lines)
    
## end