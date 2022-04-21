
#Here is a simple program that displays the camera feed in a cv2.namedWindow and will take a snapshot when you hit SPACE. It will also quit if you hit ESC.

import cv2
import os
import time

sleepcounter = 0
cam = cv2.VideoCapture(0)
path = 'C:/OpenCVImages/'
cv2.namedWindow("test")
try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)



    if True:
        # SPACE pressed
        time.sleep(1)
        sleepcounter=sleepcounter+1
        if sleepcounter == 30:
            sleepcounter = 0


            timestr = time.strftime("%Y%m%d-%H%M%S")
            img_name = "opencv_frame_{}_{}.png".format(timestr,img_counter)
            cv2.imwrite(os.path.join(path , img_name), frame)
            #cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

cam.release()

cv2.destroyAllWindows()
