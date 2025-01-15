import cv2 as cv

def blur_face(img):
    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)
    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1

    return cv.GaussianBlur(img, (dW, dH), 0)

# Initialize the webcam (0 is the default camera)
cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('face/haar_face.xml')

while True:
    ret, img = cap.read()

    faces = haar_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20,20))

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        # img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])

    cv.imshow('Camera', img)


    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break

# Release the webcam and close windows
cap.release()
cv.destroyAllWindows()
