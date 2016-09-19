# _*_ coding: utf-8 _*_

import cv2
from pprint import pprint

im = cv2.imread('img-02879.jpg')
height, width, channels = im.shape

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,150,255,0)
thresh = thresh[250: height, 0:width]

# thresh = cv2.resize(thresh, None, fx = 0.5, fy = 0.5)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
# pprint(contours)
img = cv2.drawContours(thresh, contours, -1, (255,255,0), 1)


# ce_img = cv2.Canny(im, 150, 300)

# contours = cv2.findContours(ce_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
# pprint(contours)
# print len(contours[0])

# img = cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

# th_area = im.shape[0] * im.shape[1] / 100
# contours_large = list(filter(lambda c:cv2.contourArea(c) > th_area, contours))

# outputs = []
# rects = []
# approxes = []

# for (i,cnt) in enumerate(contours_large):
#     arclen = cv2.arcLength(cnt, True)
#     approx = cv2.approxPolyDP(cnt, 0.02*arclen, True)
#     if len(approx) < 4:
#         continue
#     approxes.append(approx)
#     rect = getRectByPoints(approx)
#     rects.append(rect)
#     outputs.append(getPartImageByRect(rect))
#     # cv2.imwrite('./out/output'+str(i)+'.jpg', getPartImageByRect(rect))
#     print "out"


cv2.imshow('canny_edges', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
