from glob import glob
import os
from os.path import basename, join, exists
from random import shuffle

targetFolder = "train"
train_frames=[]
val_frames  =[]
test_frames =[]
all_videos  = {}

img=[]


file_ = open("driver_imgs_list.csv")
lines = file_.readlines()
lines = lines[1:]

for line in lines:
    splited = line.split(",")

    driver_id = splited[0]
    class_    = splited[1]
    image     = splited[2]

    if driver_id not in all_videos.keys():
        all_videos[driver_id] = []
        img = []

    img.append((str(class_) + "/" + str(image)).split("\n")[0])
    all_videos[driver_id] = img

items = all_videos.keys()
counter=0

for i in range(len(all_videos)):
    for idx, val in enumerate(all_videos[items[i]]):
        if counter < (len(all_videos)-2):
            train_frames.append(val)
            print(counter)
        elif (counter < (len(all_videos)-1)):
            val_frames.append(val)
        else:
            test_frames.append(val)
    
    counter+=1


classes = {"c0":0,"c1":1,"c2":2,"c3":3,
"c4":4,"c5":5,"c6":6,"c7":7,"c8":8,"c9":9}

shuffle(test_frames)
shuffle(val_frames)
shuffle(train_frames)

f = open("new_stateFarm_train.txt", "w")
p = open("new_stateFarm_val.txt", "w")
g = open("new_stateFarm_test.txt", "w")

train_lines=[]
val_lines=[]
test_lines=[]

for value in train_frames:
    v_ = value.split("/")
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[0]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    train_lines.append(str_)

for value in val_frames:
    v_ = value.split("/")
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[0]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    val_lines.append(str_)

for value in test_frames:
    v_ = value.split("/")
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[0]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    test_lines.append(str_)

f.writelines(train_lines)
p.writelines(val_lines)
g.writelines(test_lines)
