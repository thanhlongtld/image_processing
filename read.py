import cv2 as cv

# img = cv.imread('images/image.jpg')

# cv.imshow("Image", img)

capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
