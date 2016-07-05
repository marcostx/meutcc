
acceptedClasses = ['ApplyEyeMakeup', 'ApplyLipstick']

f = open("ucf101_split_testVideos.txt", 'r')
g = open("ucf101_split_test_videos.txt", 'w')

f_lines = f.readlines()

new_data=[]
for i in f_lines:
	if i.split('/')[0].split("_")[1] in acceptedClasses:
		g.write(i)

f.close()
g.close()