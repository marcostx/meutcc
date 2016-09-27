import Tkinter
import tkMessageBox
import numpy as np
import caffe
import glob
import pylab as pl
from tkFileDialog import askdirectory
import cv2
import sys




classes = {0: "safe driving", 1:"texting right", 2: "talking on the phone right", 
3: "texting (left)",4: "talking on the phone (left)",5: "operating the radio",
6: "drinking",7: "reaching behind",8: "hair and makeup",9: "talking to passenger"}

if len(sys.argv) > 1:
	op = sys.argv[1]
	if op == "2" and len(sys.argv) > 2:
		filename = sys.argv[2]
	elif op == "2" and len(sys.argv) <= 2:
		print("Error: Usage python interface 2 [video_frames_path]")
		exit()

else:
	print("Error: Usage python interface [op] ")
	exit()


def initialize_transformer(image_mean, is_flow):
  shape = (1, 3, 227, 227)
  transformer = caffe.io.Transformer({'data': shape})
  
  channel_mean = np.zeros((3,227,227))
  for channel_index, mean_val in enumerate(image_mean):
    channel_mean[channel_index, ...] = mean_val
  
  transformer.set_mean('data', channel_mean)
  transformer.set_raw_scale('data', 255)
  transformer.set_channel_swap('data', (2, 1, 0))
  transformer.set_transpose('data', (2, 0, 1))

  return transformer

ucf_mean_RGB = np.zeros((3,1,1))
ucf_mean_RGB[0,:,:] = 103.939
ucf_mean_RGB[1,:,:] = 116.779
ucf_mean_RGB[2,:,:] = 128.68

transformer_RGB = initialize_transformer(ucf_mean_RGB, False)

# Extract list of frames in video
RGB_images = []

#classify images with singleFrame model
def singleFrame_classify_images(net, transformer):
	if op == "1":
		mean_val = 0
		_ = 0
	  	cap = cv2.VideoCapture(0)

		while(True):
		    # Capture frame-by-frame
		    ret, frame = cap.read()
		    
		    input_im = caffe.io.resize_image(frame, (277,277))
		    caffe_in = transformer.preprocess('data',input_im)
		    net.blobs['data'].data[...] = caffe_in

		    out = net.forward()
		    # getting the probabilities
		    val =out['probs'][0][:10]
		    sorted_ = np.sort(val)

		    # Our operations on the frame come here
		    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		    font = cv2.FONT_HERSHEY_SIMPLEX
		    cv2.putText(frame,str(classes[np.where(val == sorted_[-1])[0][0]] + ":" + str(val[np.where(val == sorted_[-1])[0][0]])),
		    	(frame.shape[1]/2,frame.shape[0]-100), font, 0.5,(0,255,0),2,cv2.LINE_AA)
		    cv2.putText(frame,str(classes[np.where(val == sorted_[-2])[0][0]] + ":" + str(val[np.where(val == sorted_[-2])[0][0]])),
		    	(frame.shape[1]/2,frame.shape[0]-80), font, 0.5,(0,255,0),2,cv2.LINE_AA)
		    cv2.putText(frame,str(classes[np.where(val == sorted_[-3])[0][0]] + ":" + str(val[np.where(val == sorted_[-3])[0][0]])),
		    	(frame.shape[1]/2,frame.shape[0]-60), font, 0.5,(0,255,0),2,cv2.LINE_AA)

		    mean_val += np.where(val == sorted_[-1])[0][0]
		    _+=1

		    frame = cv2.resize(frame, (640,480))
		    # Display the resulting frame
		    cv2.imshow('frame',frame)
		    cv2.resizeWindow('frame', 400, 400)
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

		mean_val = mean_val/_
		cap.release()
		cv2.destroyAllWindows()

		return mean_val
	elif op == "2":
		frames = glob.glob('%s/*.jpg' %(filename))
		output_predictions = np.zeros((len(frames),10))
		mean_val = 0
	  	c = 0
	  	for im in frames:
			# reading the image
			frame = cv2.imread(im,1)
			input_im = caffe.io.load_image(im)

			#resizing if it's necessary
			imageResized = caffe.io.resize_image(input_im, (277,277))
			caffe_in = transformer.preprocess('data',imageResized)
			net.blobs['data'].data[...] = caffe_in
			    
			out = net.forward()
			# getting the probabilities
			val =out['probs'][0][:10]

			output_predictions[c]=val
			sorted_ = np.sort(val)

			#gray = cv2.cvtColor(input_im, cv2.COLOR_BGR2GRAY)
			
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,str(classes[np.where(val == sorted_[-1])[0][0]] + ":" + str(val[np.where(val == sorted_[-1])[0][0]])),
				(frame.shape[1]/9,frame.shape[0]-100), font, 0.5,(0,255,0),2,cv2.LINE_AA)
			cv2.putText(frame,str(classes[np.where(val == sorted_[-2])[0][0]] + ":" + str(val[np.where(val == sorted_[-2])[0][0]])),
				(frame.shape[1]/9,frame.shape[0]-80), font, 0.5,(0,255,0),2,cv2.LINE_AA)
			cv2.putText(frame,str(classes[np.where(val == sorted_[-3])[0][0]] + ":" + str(val[np.where(val == sorted_[-3])[0][0]])),
				(frame.shape[1]/9,frame.shape[0]-60), font, 0.5,(0,255,0),2,cv2.LINE_AA)

			mean_val += np.where(val == sorted_[-1])[0][0]
			cv2.imshow('frame',frame)
			if cv2.waitKey(5) & 0xFF == ord('q'):
				break

			del input_im
			c+=1

		mean_val = mean_val/len(frames)

	return mean_val

def classifyVideo():
	#Models and weights
	singleFrame_model = 'deploy_singleFrame.prototxt'
	RGB_singleFrame = 'no_data_augm_iter_1000.caffemodel'

	RGB_singleFrame_net =  caffe.Net(singleFrame_model, RGB_singleFrame, caffe.TEST)

	output = singleFrame_classify_images(RGB_singleFrame_net, transformer_RGB)
	print(output)
	del RGB_singleFrame_net

   	#tkMessageBox.showinfo( "Hello Python", filename)

if __name__ == '__main__':
	classifyVideo()