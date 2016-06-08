import cv2
import numpy as np
from matplotlib import pyplot as plt
import json
from saveToDatabase import SaveToDatabase

d = dict()
with open('calibrationNew.json') as json_data:
    d = json.load(json_data)
    print(d)

rightCoordinates = d['right']
leftCoordinates = d['left']
middleCoordinates = d['middle']

def loadImages(side):
    images = []
    stages = 10
    for i in range(stages):
        # images.append(cv2.imread('newCuts/' +side + '/' + str(i + 1) + '.jpg',0))
        images.append(cv2.imread('../newMosqueOrientation/' +side + '/' + str(i + 1) + '.jpg',0))

    return images

def checkForOneImage(img, img_Gray, isLeft, stageNo, isMiddle):
    w, h = img.shape[::-1]
    if isLeft:
        coord = leftCoordinates[stageNo - 1]
        threshold = 0.6
    else:
        coord = rightCoordinates[stageNo - 1]
        threshold = 0.7

    if isMiddle:
        coord = middleCoordinates[stageNo - 1]
        threshold = 0.7

    sliced = img_Gray[coord[0][0] : coord[0][0] + coord[1][0], coord[0][1] : coord[0][1] + coord[1][1]]
    res = cv2.matchTemplate(sliced,img,cv2.TM_CCOEFF_NORMED)

    loc = np.where( res >= threshold)
    return len(loc[0]) >= 1

def checkOneStage(stageNo, img_Gray, leftImage, rightImage):
    #leftImage = cv2.imread('left/' + str(stageNo) + '.jpg',0)
    #rightImage = cv2.imread('right/' + str(stageNo) + '.jpg',0)
    leftFound = checkForOneImage(leftImage, img_Gray, True, stageNo, False)
    rightFound = checkForOneImage(rightImage, img_Gray, False, stageNo, False)
    #rightFound = False
    return leftFound, rightFound

def getStage(img_gray, leftImgs, rightImgs):
    stage = 10
    while stage > 0:
        #if stage == 2 or stage == 6:
        #    stage += 1
        #    continue
        left, right = checkOneStage(stage, img_gray, leftImgs[stage - 1], rightImgs[stage - 1])
        if left or right:
            if left and right:
                return ('both ' + str(stage), left, right, stage)
            if left:
                return ('left ' + str(stage), left, right, stage)
            if right:
                return ('right ' + str(stage), left, right, stage)
        stage -= 1

    return -1, False, False, -1

def getStartPoint():
    return 11

def getNumberOfPeoplePerRow():
    return 35

def estimatePeople(stage, left, right, middleFound):

    statusFraction = 0
    rowStatus = ''
    startPoint = getStartPoint()
    numberOfPeoplePerRow = getNumberOfPeoplePerRow()
    numberOfFullRows = startPoint - stage - 1
    lastStage = 10
    total = numberOfFullRows * numberOfPeoplePerRow
    if left and right:
        if not middleFound:
            total += (numberOfPeoplePerRow/3)
            rowStatus += 'One-third filled'
            statusFraction = 0.3
    elif left:
        if not middleFound:
            total += (3*numberOfPeoplePerRow/5)
            rowStatus += 'Three-fifth filled'
            statusFraction = 0.6
        else:
            total += (0)
    elif right:
        if not middleFound:
            total += (3*numberOfPeoplePerRow/5)
            rowStatus += 'Three-fifth filled'
            statusFraction = 0.6
    else:
        if stage == lastStage:
            total += (numberOfPeoplePerRow/3)
            rowStatus += 'one-third filled'
            statusFraction = 0.3


    return total, rowStatus, statusFraction



def colorTheRegion(image, stage, left, right, middle):
    stage = int(stage)
    if stage == -1:
        return
    if left:
        coord = leftCoordinates[stage - 1]
        #pt = ( coord[0][1], coord[0][0])
        pt = (coord[0][1], coord[0][0])
        w = coord[1][1]
        h = coord[1][0]
        #pt = ( coord[0][1], coord[0][0])
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    if right:
        coord = rightCoordinates[stage - 1]
        pt = ( coord[0][1], coord[0][0])
        w = coord[1][1]
        h = coord[1][0]
        #pt = ( coord[0][1], coord[0][0])
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    if middle:
        coord = middleCoordinates[stage - 1]
        pt = (coord[0][1], coord[0][0])
        w = coord[1][1]
        h = coord[1][0]
        #pt = ( coord[0][1], coord[0][0])
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

def getFirstString(stageInt):
    st = ''
    lastRow = 10
    for i in range(lastRow - stageInt):
        st += 'Row ' + str(i+1) + ' completely filled \n'

    st = ''
    return st

leftImages = loadImages('left')
rightImages = loadImages('right')
middleImages = loadImages('middle')


fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('../outputVideos/output3.avi',fourcc, 20.0, (800,600))

# cap = cv2.VideoCapture('../../bigVideo/prayer.avi')
# cap = cv2.VideoCapture('../../bigVideo/full_pray.avi')
cap = cv2.VideoCapture('../GenerateVideo/backprayer.avi')
# cap = cv2.VideoCapture('../vid/prayFirst.avi')
font = cv2.FONT_HERSHEY_SIMPLEX
i = 0


saveValues = SaveToDatabase()
while True:
    success,image = cap.read()
    i += 1
    if not success:
        break
    #if i % 500 != 0:
    #    continue
    # print i
    if success:
        grayDiff = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        stage, left, right, stageInt = getStage(grayDiff, leftImages, rightImages)
        middleFound = checkForOneImage(middleImages[stageInt - 1], grayDiff, True, stageInt, True)
        colorTheRegion(image, stageInt, left, right, middleFound)

        # est = estimatePeople(stageInt, left, right, middleFound)
        est, rowStat, statusFraction = estimatePeople(stageInt, left, right, middleFound)
        #est = -9
        firstString = getFirstString(stageInt);
        num = 10-stageInt
        num += statusFraction
        # firstString += 'Row ' + str(10-stageInt + 1) + ': ' + rowStat
        firstString +=  str(num) + ' rows filled'
        stringToWrite = firstString + ' \nEstimate per row: 35'
        y0, dy = 40, 40
        for j, line in enumerate(stringToWrite.split('\n')):
            y = y0 + j*dy
            cv2.putText(image, line, (10, y ), font, 1, (255,0,0),2)
        # cv2.putText(image,stringToWrite,(10,500), font, 1,(255,255,255),2)
        saveValues.insertIntoImagesTable('imageCounter', i,stageInt, 1,0,1)
        cv2.imshow('frame',image)
        out.write(image)
        #if i % 500 == 0:
        #cv2.imwrite(("prayerImg/image" + str(i) + '.jpg'), image)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

saveValues.closeAll()
cap.release()
out.release()
cv2.destroyAllWindows()