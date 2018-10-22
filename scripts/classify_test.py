# Classify test images
import numpy as np
import glob
import sys
import caffe
import pickle

#initial = 40000
#final = 79727

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

  return transformer

ucf_mean_RGB = np.zeros((3,1,1))
ucf_mean_RGB[0,:,:] = 103.939
ucf_mean_RGB[1,:,:] = 116.779
ucf_mean_RGB[2,:,:] = 128.68

transformer_RGB = initialize_transformer(ucf_mean_RGB, False)
test="test"

# Extract list of frames in video
RGB_images = glob.glob('%s/*.jpg' %(test))

#classify images with singleFrame model
def singleFrame_classify_images(frames, net, transformer):

  input_images = []
  c=0
  output_predictions = np.zeros((len(frames),10))
  for im in frames:
    print("reading : %d", im)
    print("classifying image : %d", c)
        # reading the image
    input_im = caffe.io.load_image(im)

    #resizing if it's necessary
    #if (input_im.shape[0] < 240):
    input_im = caffe.io.resize_image(input_im, (277,277))
    caffe_in = transformer.preprocess('data',input_im)
    net.blobs['data'].data[...] = caffe_in
      
    out = net.forward()
    # getting the probabilities
    val =out['probs'][0][:10]

    output_predictions[c]=val
    print(np.argmax(val))
    del input_im
    c+=1

  return output_predictions

#Models and weights
singleFrame_model = 'deploy_singleFrame.prototxt'
RGB_singleFrame = 'no_data_augm_iter_1000.caffemodel'

RGB_singleFrame_net =  caffe.Net(singleFrame_model, RGB_singleFrame, caffe.TEST)

output = singleFrame_classify_images(RGB_images, RGB_singleFrame_net, transformer_RGB)
del RGB_singleFrame_net


# saving preds
submission = open('sample_submission.csv','r+')
test = open('test.csv', 'a')
lines = submission.readlines()
#test.writelines(lines[0])
for idx, v in enumerate(range(len(RGB_images))):
  newLine=[]

  for index, pp in enumerate(output[idx]):
    newLine.append(str(pp))
  newLine = RGB_images[v].split("/")[1] + ',' + ','.join(newLine) + "\n"
  test.writelines(newLine)
