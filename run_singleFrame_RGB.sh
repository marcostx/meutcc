#!/bin/sh

TOOLS=../caffe/build/tools

GLOG_logtostderr=1 $TOOLS/caffe train -solver solver_CNN.prototxt -weights caffe_imagenet_hyb2_wr_rc_solver_sqrt_iter_310000
echo 'Done.'
