outp = open("output5.txt","r")
out_lines = outp.readlines()

lossAndAccuracy = []
train_accuracy = []
test_accuracy = []
train_loss = []
test_loss = []
iteration = []

for idx, line in enumerate(out_lines):
	n_ = line.split("]")[1]
	spaces_split = n_.split(" ")
	if ("accuracy" in spaces_split) or ("loss" in spaces_split):
		lossAndAccuracy.append(' '.join(spaces_split))

for idx,i in enumerate(lossAndAccuracy):

	line = i.split(" ")
	if ("accuracy" in line) and ("Test" in line):
		test_accuracy.append(line[-1])
	elif ("accuracy" in line) and ("Train" in line):
		train_accuracy.append(line[-1])


for idx,i in enumerate(lossAndAccuracy):

	line = i.split(" ")
	if ("loss" in line) and ("Test" in line):
		l = i.split("=")[1].split(" ")[1]
		test_loss.append(l)
	elif ("loss" in line) and ("Iteration" in line):
		train_loss.append(line[-1].split("\n")[0])

for idx,i in enumerate(lossAndAccuracy):

	line = i.split(" ")
	if "Iteration" in line:
		iteration.append(line[2].split(",")[0])

import pylab

pylab.plot(range(0,1001,10), test_loss,'-r', label="Validation loss")
pylab.plot(range(0,1001,2),train_loss,'-b', label="Train loss")
pylab.legend(loc="upper right")
pylab.xlabel("iterations")
pylab.ylabel("Train/Validation loss")
pylab.ylim(0.0,2.0)
pylab.xlim(0, 1000)


pylab.show()
	