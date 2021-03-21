import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread('images/image_large.jpg')
cv.imshow("ME", img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAb", lab)

# BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

cv.waitKey(0)
