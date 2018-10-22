#!/usr/bin/env python

import numpy as np
import sys
from glob import glob
from os.path import basename, join, exists
from os import makedirs
import cv2

FLOW_IMAGES_PATH = 'flow_train'

def dense_flow(hsv, flow):
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang * 180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv ,cv2.COLOR_HSV2BGR)
    return bgr

if __name__ == '__main__':
    
    train_frames=[]
    test_frames=[]
    all_videos = {}

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
two_by_two_Values=[]
aux=[]
drivers_two_by_two_values={}

for i in range(len(all_videos)):
    for idx, val in enumerate(all_videos[items[i]]):
        class_ = val.split("/")[0]
        if idx+1 < len(all_videos[items[i]]) and (all_videos[items[i]][idx+1].split("/")[0] == class_):
            aux.append(val)
        else:
            aux.append(val)
            two_by_two_Values.append(aux)
            aux=[]
            continue
    drivers_two_by_two_values[items[i]] = two_by_two_Values
    two_by_two_Values=[]

# create flow images
if not exists(FLOW_IMAGES_PATH):
    makedirs(FLOW_IMAGES_PATH)

for i in range(len(drivers_two_by_two_values)):
    for pp in range(0,10):
        prev = cv2.imread("train/" + drivers_two_by_two_values[items[i]][pp][0])
        prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        hsv = np.zeros_like(prev)
        hsv[...,1] = 255
        for qq in range(len(drivers_two_by_two_values[items[i]][pp])):
            if qq>0:
                img = cv2.imread("train/"+drivers_two_by_two_values[items[i]][pp][qq])
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None,0.5, 3, 15, 3, 5, 1.2, 0)
                prevgray = gray

                if not exists(FLOW_IMAGES_PATH + '/' +str(drivers_two_by_two_values[items[i]][pp][qq].split("/")[0])):
                    makedirs(FLOW_IMAGES_PATH + '/' + str(drivers_two_by_two_values[items[i]][pp][qq].split("/")[0]))
    
                flow_path = (FLOW_IMAGES_PATH+ '/' + str(drivers_two_by_two_values[items[i]][pp][qq].split("/")[0]) + "/")

                newName = drivers_two_by_two_values[items[i]][pp][qq].split("/")[1].split(".jpg")[0] + " " +drivers_two_by_two_values[items[i]][pp][qq-1].split("/")[1]
                newName = newName.split(" ")
                newName = newName[0]+"_"+newName[1]
                
                cv2.imwrite(flow_path + str(newName), dense_flow(hsv, flow))
                prev = img

cv2.destroyAllWindows()

