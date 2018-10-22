from glob import glob
import os
from os.path import basename, join, exists
from random import shuffle

targetFolder = "flow_train"
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

train=0
test=0
for i in xrange(len(all_videos)):

	size = (len(glob(all_videos[i] + "/*")))
	for idx, vid in enumerate(glob(all_videos[i] + "/*")):
		if idx < (((size)*80)/100):
			train+=1
			train_frames.append(vid)
        	else:
			test+=1
			test_frames.append(vid)
	train=0
	test=0

classes = {"c0":0,"c1":1,"c2":2,"c3":3,
"c4":4,"c5":5,"c6":6,"c7":7,"c8":8,"c9":9}

shuffle(test_frames)
shuffle(train_frames)

f = open("stateFarm_train.txt", "w")
g = open("stateFarm_test.txt", "w")
train_values = []
train_lines=[]
test_lines=[]

print(len(train_frames))
for value in train_frames:
    v_ = value.split("/")[1:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    train_lines.append(str_)

print(len(test_frames))
for value in test_frames:
    v_ = value.split("/")[1:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    test_lines.append(str_)

f.writelines(train_lines)
g.writelines(test_lines)
