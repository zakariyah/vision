__author__ = 'abu-abdurahman'
import cv2
import numpy as np
from matplotlib import pyplot as plt
import json

#rightCoordinates = [[(401, 640),
#                     (21, 66)], [(324, 631), (18, 105)], [(272, 614), (18, 108)], [(228, 642), (16, 65)], [(194, 613), (13, 75)], [(160, 551), (17, 60)], [(138, 536), (13, 58)], [(122, 540), (14, 59)], [(110, 537), (12, 57)], [(96, 490), (9, 71)]]

#leftCoordinates = [[(390, 94), (13, 84)], [(316, 65), (15, 151)], [(262, 84), (18, 157)], [(216, 153), (15, 133)], [(182, 177), (13, 107)], [(154, 192), (13, 99)], [(138, 181), (13, 72)], [(118, 214), (14, 90)], [(102, 246), (10, 71)], [(94, 229), (11, 60)]]

#middleCoordinates =  [[(415, 337), (26, 185)], [(329, 363), (25, 159)], [(263, 319), (20, 174)], [(212, 322), (19, 171)], [(175, 317), (16, 143)], [(147, 331), (13, 124)], [(129, 343), (9, 124)], [(110, 354), (10, 108)], [(95, 358), (11, 117)], [(83, 387), (12, 64)]]

#img_rgb = cv2.imread('../newBackground600600.jpg')

def getLeftRightAndMiddleCoordinates(backGroundImage):
    left = []
    right = []
    middle = []
    img_rgb = cv2.imread(backGroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    side = ['left', 'middle', 'right']
    valA = [0,0,0]
    for a in range(3):
        sideToUse = side[a]
        valA[a] = []
        for i in range(10):
            template = cv2.imread('newCuts/' + sideToUse + '/' + str(i+1) +'.jpg',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            gotten = False
            for threshold in range(100,50, -1):
                threshold /= 100.0
                loc = np.where( res >= threshold)

                if len(loc[0]) >= 1:

                    arr = [(loc[0][0], loc[1][0]), (h, w)]
                    valA[a].append(arr)
                    gotten = True

                    for pt in zip(*loc[::-1]):

                        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                    break


            if not gotten:
                print i + 1, ' not gotten'
            #threshold = 0.8

    dictToReturn = dict()
    for x in range(len(side)):
        dictToReturn[side[x]] = valA[x]

    return dictToReturn
    #print i + 1, len(loc[0])
    #for pt in zip(*loc[::-1]):
    #    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #
    cv2.imwrite('res' + str(i+1) +'.png',img_rgb)

outputfilename = 'calibration.json'

with open(outputfilename, 'wb') as outfile:
    json.dump(getLeftRightAndMiddleCoordinates('restry.jpg'), outfile)