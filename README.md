# Distracted Driver Detection with Deep Learning ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

Here, the challenge is to classify each driver's behavior. Are they driving attentively, wearing their seatbelt, or taking a selfie with their friends in the backseat?


## Installation

### Requirements
* scikit-learn
* Python >= 2.7
* Caffe
* matplotlib
* OpenCV >= 3.0   

## Instructions  

1. Download the data : https://www.kaggle.com/c/state-farm-distracted-driver-detection
2. Prepare data:

If "stateFarm_train.txt" and "stateFarm_test.txt" are not generated, run:

```
$ python prepare_data.py
```


3. Train RGB model
```
$ ./run_singleFrame_RGB.sh
```
Make sure to change the "root_folder" param in "CNN.prototxt" as needed.


4. Evaluate on test
```
$ python classify_test.py
```

This script classifies the test imgs and fill the submission csv for Kaggle.




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

_Obs.: The models are highly based on ([LRCN])(https://github.com/LisaAnne/lisa-caffe-public/tree/lstm_video_deploy/examples/LRCN_activity_recognition) repository_

## Contact
Marcos Teixeira ([ecclesiedei@gmail.com])(ecclesiedei@gmail.com)
