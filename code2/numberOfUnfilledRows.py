import cv2
import numpy as np
from matplotlib import pyplot as plt

leftCoordinates = [
    ((908, 101), (44, 284)),
    ((778, 186), (50, 235)),
    ((658, 316), (44, 329)),
    ((563, 330), (42,295)),
    ((458, 496), (44, 308)),
    ((399, 472), (40, 287)),
    ((348, 530), (40, 297)),
    ((297, 602), (44, 200)),
    ((283, 610), (25, 193)),
    ((262, 626), (20, 114))
]

rightCoordinates = [
    ((962, 1518), (70, 251)),
    ((794, 1474), (58, 259)),
    ((651, 1347), (50, 230)),
    ((529, 1392), (46, 257)),
    ((444, 1337), (50, 242)),
    ((393, 1493), (56, 138)),
    ((346,1433), (43, 186)),
    ((303, 1372), (33, 184)),
    ((271, 1441), (31, 95)),
    ((243, 1401), (27, 116))
]

#img_rgb = cv2.imread('frame20sec.jpg')
img_rgb = cv2.imread('prayerImg/image19500.jpg')
#img_rgb = cv2.imread('prayerImg/image1000.jpg')
#img_rgb = cv2.imread('prayerImg/image11500.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

for i in range(10):
    template = cv2.imread('right/' + str(i+1) +'.jpg',0)
    #template = cv2.imread('left/' + str(i+1) +'.jpg',0)
    w, h = template.shape[::-1]
    #print w,h
    coord = rightCoordinates[i]
    #coord = leftCoordinates[i]
    sliced = img_gray[coord[0][0] : coord[0][0] + coord[1][0], coord[0][1] : coord[0][1] + coord[1][1]]
    res = cv2.matchTemplate(sliced,template,cv2.TM_CCOEFF_NORMED)
    gotten = False
    for threshold in range(100,50, -1):
        threshold /= 100.0
        loc = np.where( res >= threshold)
        #print loc
        if len(loc[0]) >= 1:
            print i+1, threshold, loc
            gotten = True
            break


    if not gotten:
        print i + 1, ' not gotten'
    #threshold = 0.8

    #print i + 1, len(loc[0])
    #for pt in zip(*loc[::-1]):
    #    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #
    #cv2.imwrite('res' + str(i+1) +'.png',img_rgb)