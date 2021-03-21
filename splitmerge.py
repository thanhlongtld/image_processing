import cv2 as cv
import numpy as np

img = cv.imread("images/image_large.jpg")
cv.imshow("me", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merged = cv.merge([b, g, r])
# cv.imshow("merged", merged)

cv.waitKey(0)
