# Classify test images
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import caffe
import pickle
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score


#Initialize transformers

def initialize_transformer():
  shape = (1, 3, 56, 92)
  transformer = caffe.io.Transformer({'data': shape})

  #transformer.set_mean('data', channel_mean)
  transformer.set_raw_scale('data', 255)
  transformer.set_channel_swap('data', (2, 1, 0))
  transformer.set_transpose('data', (2, 0, 1))

  return transformer

transformer_RGB = initialize_transformer()
train="stateFarm_train.txt"

file_ = open(train,'r')
lines = file_.readlines()
values=[]
y_true=[]
for val in lines:
  values.append("battrain/" + val.split(" ")[0])
  y_true.append(int(val.split(" ")[1]))

RGB_images = values

#classify images with singleFrame model
def singleFrame_classify_images(frames, net, transformer):

  input_images = []
  c=0
  output_predictions = np.zeros(len(frames))
  for im in frames:
    # reading the image
    input_im = caffe.io.load_image(im)

    input_im = caffe.io.resize_image(input_im, (56,92))
    caffe_in = transformer.preprocess('data',input_im)
    net.blobs['data'].data[...] = caffe_in

    out = net.forward()
    # getting the probabilities
    val =out['probs'][0][:10]

    output_predictions[c]=np.argmax(val)

    del input_im
    c+=1

  return output_predictions

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(10)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#Models and weights
singleFrame_model = 'deploy_singleFrame.prototxt'
RGB_singleFrame = 'bat_model_iter_984.caffemodel'

RGB_singleFrame_net =  caffe.Net(singleFrame_model, RGB_singleFrame, caffe.TEST)

output = singleFrame_classify_images(RGB_images, RGB_singleFrame_net, transformer_RGB)
del RGB_singleFrame_net

matrix = confusion_matrix(y_true,output)
precision = precision_score(y_true, output)
f1 = f1_score(y_true, output)
recall = recall_score(y_true, output)

print(precision)
print("\n")
print(f1)
print("\n")
print(recall)
print("\n")
print(matrix)
