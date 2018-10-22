  # Distracted Driver Detection with Deep Learning ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

Here, the challenge is to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?


## Installation

### Requirements
* scikit-learn
* Python >= 2.7
* Caffe
* matplotlib
* OpenCV >= 3.0   

## Preparation  

1. Download the data in : https://www.kaggle.com/c/state-farm-distracted-driver-detection

1. Extract frames from videos
```
$ python extract_frames.py
```
2. Train RGB model
```
$ ./run_singleFrame_RGB.sh
```
3. Evaluate the model
```
$ python generate_confusion_matrix.py
$ python generate_metrics.py
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
[Marcos Teixeira](ecclesiedei@gmail.com)
