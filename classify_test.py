# Classify test images
import numpy as np
import glob
import sys
import caffe
import pickle

RGB_video_path = 'frames/'
flow_video_path = 'flow_images/'
if len(sys.argv) > 1:
  video = sys.argv[1]
else:
  video = 'v_Archery_g01_c01'

#Initialize transformers

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
  #transformer.set_is_flow('data', is_flow)
  return transformer


ucf_mean_RGB = np.zeros((3,1,1))
ucf_mean_RGB[0,:,:] = 103.939
ucf_mean_RGB[1,:,:] = 116.779
ucf_mean_RGB[2,:,:] = 128.68

transformer_RGB = initialize_transformer(ucf_mean_RGB, False)
test="test2"

# Extract list of frames in video
RGB_images = glob.glob('%s/*.jpg' %(test))

#classify images with singleFrame model
def singleFrame_classify_images(frames, net, transformer):

  input_images = []
  for im in frames:
  	# reading the image
    input_im = caffe.io.load_image(im)

    #resizing if it's necessary
    if (input_im.shape[0] < 240):
      input_im = caffe.io.resize_image(input_im, (277,277))

    # adding to a list of images  
    input_images.append(input_im)

  
  # initialize the predictions arr
  output_predictions = []
  for i in range(0,len(input_images)):
    inp_image = input_images[i]

    caffe_in = transformer.preprocess('data',inp_image)
    net.blobs['data'].data[...] = caffe_in
    
    out = net.forward()

    # getting the probabilities
    output_predictions.append(out['probs'].argmax())

  print output_predictions

  #return output_predictions

#Models and weights
singleFrame_model = 'deploy_singleFrame.prototxt'
RGB_singleFrame = 'model_stateFarm_iter_100.caffemodel'

RGB_singleFrame_net =  caffe.Net(singleFrame_model, RGB_singleFrame, caffe.TEST)

singleFrame_classify_images(RGB_images, RGB_singleFrame_net, transformer_RGB)
del RGB_singleFrame_net


def compute_fusion(RGB_pred, flow_pred, p):
  return np.argmax(p*np.mean(RGB_pred,0) + (1-p)*np.mean(flow_pred,0))  




