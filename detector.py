import cv2

face_detector_file = "./haarcascade_frontalface_default"
face_detector = cv2.CascadeClassifier(face_detector_file)


# access the webcam.
webcam= cv2.VideoCapture(0)

# get the current frame 
while True:
    # Read the current frame 
    successful_frame_read, frame = webcam.read()
    
    # end if there's an error
    if not successful_frame_read:
        break

    # if frame read was successful  convert frame to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display frame
    cv2.imshow("Galvic Smile Detector", grayscaled_frame)


# read next frame every 1 millisecond
cv2.waitKey(1)
# release the webcam after done
webcam.release()
# destroy/close all windows
cv2.destroyAllWindows()

# code ran without errors
print("Code Completed!")