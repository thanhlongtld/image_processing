import cv2 as cv

img = cv.imread('images/image_large.jpg')

cv.imshow("Image", img)

# Converting a image to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grey", gray)

# Blur

# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# Crop
crop= img[50:200,200:400]
cv.imshow("Crop", crop)

cv.waitKey(0)
