import cv2 as cv

# Reading Images
# img = cv.imread('photos/cat2.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)
# Reading Videos

capture = cv.VideoCapture('videos/i-cover.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

