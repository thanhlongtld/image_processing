import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Works for live videos
    capture.set(3, width)
    capture.set(4, height)
    


img = cv.imread("images/image_large.jpg")
cv.imshow("Large", img)
resized_img = rescaleFrame(img)

cv.imshow("Rescale", resized_img)


capture = cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow("Video rescale", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
