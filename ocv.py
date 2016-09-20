# _*_ coding: utf-8 _*_

import cv2
from pprint import pprint


def getRectByPoints(points):
    # prepare simple array 
    points = list(map(lambda x: x[0], points))

    points = sorted(points, key=lambda x:x[1])
    top_points = sorted(points[:2], key=lambda x:x[0])
    bottom_points = sorted(points[2:4], key=lambda x:x[0])
    points = top_points + bottom_points

    left = min(points[0][0], points[2][0])
    right = max(points[1][0], points[3][0])
    top = min(points[0][1], points[1][1])
    bottom = max(points[2][1], points[3][1])
    return (top, bottom, left, right)

def getPartImageByRect(im, rect):
    return im[rect[0]:rect[1], rect[2]:rect[3]]


im = cv2.imread('img-02879.jpg')
height, width, channels = im.shape

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,150,255,0)
# thresh = thresh[250: height, 0:width]
# im = im[250: height, 0:width]

# thresh = cv2.resize(thresh, None, fx = 0.5, fy = 0.5)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHgsAIN_APPROX_SIMPLE)[0]
# pprint(contours)
img = cv2.drawContours(thresh, contours[0], -1, (255,255,0), 1)


# ce_img = cv2.Canny(im, 150, 300)

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# pprint(contours)

th_area =  (im.shape[1] / 5) * 2
print th_area
contours_large = list(filter(lambda c:cv2.contourArea(c) > th_area, contours[0]))

outputs = []
rects = []
approxes = []

for (i,cnt) in enumerate(contours_large):
    arclen = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*arclen, True)
    if len(approx) < 4:
        continue
    approxes.append(approx)
    rect = getRectByPoints(approx)
    rects.append(rect)
    outputs.append(getPartImageByRect(im,rect))
    # cv2.imwrite('./out/output'+str(i)+'.jpg', getPartImageByRect(rect))
for (point) in rects:
	cv2.rectangle(im, (point[0], point[1]), (point[2], point[3]), (0,0,255), 3, 4)
	pprint(point)


cv2.imshow('canny_edges', cv2.resize(thresh, None, fx = 0.5, fy = 0.5))
im = cv2.resize(im, None, fx = 0.5, fy = 0.5)
cv2.imshow("img", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
