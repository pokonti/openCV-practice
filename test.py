import cv2 as cv

# Initialize the webcam (0 is the default camera)
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Press 'q' to quit")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv.imshow('Webcam Feed', frame)

    # Exit when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv.destroyAllWindows()
