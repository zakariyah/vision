import cv2
import numpy as np
from matplotlib import pyplot as plt
import json
import math


#cap = cv2.VideoCapture('../bigVideo/prayer.avi')
# cap2 = cv2.VideoCapturehttp://stackoverflow.com/questions/4195453/how-to-resize-an-image-with-opencv2-0-and-python2-6('../bigVideo/full_pray.avi')
# cap = cv2.VideoCapture('./GenerateVideo/frontreal.avi')
cap = cv2.VideoCapture('./GenerateVideo/darkToLight.avi')
# cap = cv2.VideoCapture('../vid/frontmini.avi')

# cap = cv2.VideoCapture('../vid/prayFirst.avi')
font = cv2.FONT_HERSHEY_SIMPLEX
i = 0
# 1. Do bg subtraction
# 2. And nms filtering
# 3. Stack the four and write to file.


fgbg = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)
# fgbg2 = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('darkTo.avi',fourcc, 20.0, (800, 600))
brightness = []
while True:
    success,image = cap.read()
    # success2,image2 = cap2.read()

    i += 1
    if not success:
        break
    #if i % 500 != 0:
    #    continue
    # print i
    if success:

        # grayDiff = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        # # stage, left, right, stageInt = getStage(grayDiff, leftImages, rightImages)
        # # middleFound = checkForOneImage(middleImages[stageInt - 1], grayDiff, True, stageInt, True)
        # # colorTheRegion(image, stageInt, left, right, middleFound)
        #
        # # est = estimatePeople(stageInt, left, right, middleFound)
        # est, rowStat = estimatePeople(stageInt, left, right, middleFound)
        # #est = -9
        # firstString = getFirstString(stageInt);
        # firstString += 'Row ' + str(10-stageInt + 1) + ': ' + rowStat
        # stringToWrite = firstString + ' \nEstimate: ' + str(est)
        # y0, dy = 40, 40
        # for j, line in enumerate(stringToWrite.split('\n')):
        #     y = y0 + j*dy
        #     cv2.putText(image, line, (10, y ), font, 1, (255,0,0),2)
        # # cv2.putText(image,stringToWrite,(10,500), font, 1,(255,255,255),2)
        # if i > 5000:
        #     break

        # if i > 4500:
        #     print 'next one'
        #     if i == 4500:
        #         fgbg = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)
        #     # fgmask = fgbg.apply(image)
        #     # fgmask = cv2.GaussianBlur(fgmask, (21,21),0)
        #     # mask2rgb = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2RGB)
        #
        #     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #convert it to hsv
        #     brightness.append(np.mean(hsv[:,:,2]))
        #
        #
        #     # visCom = np.concatenate((vis, vis2rgb), axis=0)
        #
        #     # cv2.imshow('frame',mask2rgb)
        #     # out.write(mask2rgb)
        #     #if i % 500 == 0:
        #     #cv2.imwrite(("prayerImg/image" + str(i) + '.jpg'), image)
    
        fgmask = fgbg.apply(image)
        # fgmask = cv2.GaussianBlur(fgmask, (21,21),0)
        mask2rgb = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2RGB)
        cv2.imshow('frame',mask2rgb)
        # out.write(mask2rgb)
            #if i % 500 == 0:

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break


# plt.plot(brightness)
# plt.ylabel('brightness over time')
# plt.show()
# plt.savefig("exercice_2.png")

cap.release()
out.release()
cv2.destroyAllWindows()