import cv2
import numpy as np
from matplotlib import pyplot as plt
import json


#cap = cv2.VideoCapture('../bigVideo/prayer.avi')
# cap = cv2.VideoCapture('../vid/frontmini.avi')
cap1 = cv2.VideoCapture('./GenerateVideo/vid1.avi')
cap2 = cv2.VideoCapture('./GenerateVideo/vid2.avi')
cap3 = cv2.VideoCapture('./GenerateVideo/vid3.avi')
cap4 = cv2.VideoCapture('./GenerateVideo/vid4.avi')
# cap2 = cv2.VideoCapture('../vid/backmini.avi')
font = cv2.FONT_HERSHEY_SIMPLEX
i = 0
# 1. Do bg subtraction
# 2. And nms filtering
# 3. Stack the four and write to file.


# fgbg = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)
# fgbg2 = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
# out = cv2.VideoWriter('joined.avi',fourcc, 20.0, (960,360))

out = cv2.VideoWriter('joined4.avi',fourcc, 20.0, (800,600))

while True:
    success1,image1 = cap1.read()
    success2,image2 = cap2.read()
    success3,image3 = cap3.read()
    success4,image4 = cap4.read()

    i += 1
    if not success1:
        break
    #if i % 500 != 0:
    #    continue
    # print i
    if success1:
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
        # fgmask = fgbg.apply(image)
        # fgmask2 = fgbg2.apply(image2)
        # h,w,d = image.shape
        # h2,w2,d2 = image2.shape


        small1 = cv2.resize(image1, (0,0), fx=0.5, fy=0.5)

        small2 = cv2.resize(image2, (0,0), fx=0.5, fy=0.5)

        small3 = cv2.resize(image3, (0,0), fx=0.5, fy=0.5)
        small4 = cv2.resize(image4, (0,0), fx=0.5, fy=0.5)

        # smallfg = cv2.resize(fgmask, (0,0), fx=0.5, fy=0.5)
        #
        # smallfg2 = cv2.resize(fgmask2, (0,0), fx=0.5, fy=0.5)
        # # print image.shape, image2.shape
        # vis = np.concatenate((small, small2), axis=1)
        vis = np.concatenate((small1, small2), axis=1)
        vis2 = np.concatenate((small3, small4), axis=1)
        #
        # vis2rgb = cv2.cvtColor(vis2,cv2.COLOR_GRAY2RGB)
        #
        visCom = np.concatenate((vis, vis2), axis=0)
        cv2.imshow('frame',visCom)
        out.write(visCom)
        print vis.shape
        #if i % 500 == 0:
        #cv2.imwrite(("prayerImg/image" + str(i) + '.jpg'), image)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()