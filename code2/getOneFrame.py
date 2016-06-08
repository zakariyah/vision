import cv2
import numpy as np
from matplotlib import pyplot as plt
import json


#cap = cv2.VideoCapture('../bigVideo/prayer.avi')
# cap = cv2.VideoCapture('../vid/frontmini.avi')
# cap = cv2.VideoCapture('./output3mini.avi')
# cap2 = cv2.VideoCapture('./prayOutput.avi')
cap2 = cv2.VideoCapture('../vid/prayFirst1.avi')
# font = cv2.FONT_HERSHEY_SIMPLEX
i = 0
# 1. Do bg subtraction
# 2. And nms filtering
# 3. Stack the four and write to file.


# fgbg = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)
# fgbg2 = cv2.BackgroundSubtractorMOG2(200,16,bShadowDetection = False)

# fourcc = cv2.cv.CV_FOURCC(*'XVID')
# out = cv2.VideoWriter('joined.avi',fourcc, 20.0, (960,360))

# out = cv2.VideoWriter('joined.avi',fourcc, 20.0, (1600,600))

while True:
    success,image = cap2.read()

    cv2.imwrite('filled.jpg', image)
    break

    i += 1
    if not success:
        break


cap2.release()
# out.release()
cv2.destroyAllWindows()