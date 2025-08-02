import numpy as np
import cv2 as cv
def webcam():
    cap = cv.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Apply binary thresholding
        # Pixels > 127 become 255 (white), others become 0 (black)
        ret, binary_image = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)    # Display the resulting frame
        cv.imshow('frame', binary_image)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


"""
def get_frame(cap):
    ret , frame = cap.read()
    return frame if ret else None
"""