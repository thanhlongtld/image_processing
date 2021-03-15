import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# img = cv.imread("images/image.jpg")
# cv.imshow("Image", img)

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0, 255, 0

# cv.imshow("Green", blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=2)
# cv.imshow("Rectangle", blank)

# 3. Draw a circle

cv.circle(blank, (blank.shape[1]//2,
                  blank.shape[0]//2), 40, (0, 0, 255), thickness=3)

cv.imshow("Circle", blank)

cv.waitKey(0)
