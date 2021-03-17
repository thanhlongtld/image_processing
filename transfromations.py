import cv2 as cv
import numpy as np

img = cv.imread('images/image_large.jpg')

cv.imshow("ME", img)

# Translation


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimesions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimesions)


translated = translate(img, 100, 100)
cv.imshow("Translate", translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("2 Rotated", rotated_rotated)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flip
flip = cv.flip(img, 1)
cv.imshow("Fip", flip)

# Crop
croped = img[200:400, 500:600]
cv.imshow("Crop", croped)

cv.waitKey(0)
