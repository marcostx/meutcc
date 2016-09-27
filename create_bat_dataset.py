from glob import glob
import os
from os.path import basename, join, exists
from random import shuffle
from sklearn.cross_validation import StratifiedKFold
import numpy as np

targetFolder = "battrain"
all_videos = []
train_videos = []
test_videos = []
train_frames1 = []
test_frames1 = []
train_frames2 = []
test_frames2 = []
train_frames3 = []
test_frames3 = []
X=[]
y=[]

EXTENSIONS = ["png"];

aux_=[]
train_items_videos=[]


# getting the classes
for vid in glob(targetFolder + "/*"):
    all_videos.append(vid)

class_=0

	
classes = {"c0":0,"c1":1,"c2":2,"c3":3,
"c4":4,"c5":5,"c6":6,"c7":7,"c8":8,"c9":9}

train=0
test=0
for i in xrange(len(all_videos)):
	
	size = (len(glob(all_videos[i] + "/*")))
	for idx, vid in enumerate(glob(all_videos[i] + "/*")):
        	if vid.split(".")[-1] in EXTENSIONS:
			X.append([vid])
            		v_ = vid.split("/")[1:]
            		v_ = v_[0]+ "/" + v_[1]

		    	class_index = vid.split("/")[1]
		    	y.append(classes[class_index])

X = np.array(X)
y = np.array(y)

skf = StratifiedKFold(y, shuffle=True, n_folds=3)
ind = 0

for train_index, test_index in skf:
	shuffle(train_index)
	shuffle(test_index)

	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]

	f = open("bat_train" + str(ind) + ".txt", "w")
	g = open("bat_test" + str(ind) + ".txt", "w")
	train_lines=[]
	test_lines=[]

	shuffle(X_train)
	shuffle(X_test)

	for value in zip(X_train,y_train):
	    v_ = value[0][0].split("/")[1:]
	    v_ = v_[0]+ "/" + v_[1]

	    class_index = value[0][0].split("/")[1]
	    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
	    train_lines.append(str_)

	for value in zip(X_test,y_test):
	    v_ = value[0][0].split("/")[1:]
	    v_ = v_[0]+ "/" + v_[1]

	    class_index = value[0][0].split("/")[1]
	    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
	    test_lines.append(str_)

	f.writelines(train_lines)
	g.writelines(test_lines)
	
	ind+=1
	
	

"""
shuffle(test_frames)
shuffle(train_frames)

f = open("bat_train.txt", "w")
g = open("bat_test.txt", "w")
train_lines=[]
test_lines=[]

for value in train_frames:
    v_ = value.split("/")[1:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    train_lines.append(str_)

for value in test_frames:
    v_ = value.split("/")[1:]
    v_ = v_[0]+ "/" + v_[1]

    class_index = value.split("/")[1]
    str_ = str(v_) + " " + str(classes[class_index]) + "\n"
    test_lines.append(str_)

f.writelines(train_lines)
g.writelines(test_lines)
"""
