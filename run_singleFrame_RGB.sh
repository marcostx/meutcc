#!/bin/sh

TOOLS=../caffe/build/tools

GLOG_logtostderr=1 $TOOLS/caffe train -solver solver_CNN.prototxt
echo 'Done.'
