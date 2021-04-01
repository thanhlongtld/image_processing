import cv2 as cv

img = cv.imread('images/dog.jfif')

cv.imshow("Image", img)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
equal_v = cv.equalizeHist(v)
merge = cv.merge([h, s, equal_v])
result = cv.cvtColor(merge, cv.COLOR_HSV2BGR)
cv.imshow("Result", result)


cv.waitKey(0)
