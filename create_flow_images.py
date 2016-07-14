#!/usr/bin/env python

import numpy as np
import sys
from glob import glob
from os.path import basename, join, exists
from os import makedirs
import cv2

help_message = '''

    Extracting flow of images

'''

def dense_flow(hsv, flow):
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang * 180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv ,cv2.COLOR_HSV2BGR)
    return bgr

if __name__ == '__main__':
    print help_message
    
    path = "train"
    classes = []
    videos  = []
    images  = []
    
    # reading the image frames
    for cl in glob(path + "/*"):
	   classes.extend([join(path, basename(cl))])

    for i in xrange(len(classes)):
	print(classes[i])
	
	if exists("flow/" + str(classes[i].split("/")[1])):
	    continue	
	prev = cv2.imread(glob(classes[i] + "/*")[0])
	prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    	hsv = np.zeros_like(prev)
    	hsv[...,1] = 255

    	for frame in glob(classes[i] + "/*"):
    	    #images.append(frame)
	    img = cv2.imread(frame)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            flow = cv2.calcOpticalFlowFarneback(prevgray, gray,0.5, 3, 15, 3, 5, 1.2, 0)
            prevgray = gray

	    if not exists("flow"):
		makedirs("flow")
	    if not exists("flow/" + str(frame.split("/")[1])):
		makedirs("flow/" + str(frame.split("/")[1]))

	    flow_path = "flow/" + str(frame.split("/")[1] + "/")
            cv2.imwrite(flow_path + str(basename(frame).split(".")[0]) + str(i) + '_flow.jpg', dense_flow(hsv, flow))

            prev = img
            #cv2.waitKey(0)

cv2.destroyAllWindows()
