import cv2
import keyboard

# haar files (face and smile)
face_detector_file = r"haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(face_detector_file)

smile_detector_file = r"haarcascade_smile.xml"
smile_detector = cv2.CascadeClassifier(smile_detector_file)


# access the webcam.
webcam= cv2.VideoCapture(0, cv2.CAP_DSHOW)

# get the current frame 
while True:
    # Read the current frame 
    successful_frame_read, frame = webcam.read()
    
    # end if there's an error
    if not successful_frame_read:
        break
    else:
        # if frame read was successful  convert frame to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(grayscaled_frame)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)

            # crop the frame to just contain the face and put smile on it
            the_face = frame[y:y+h, x:x+w]
            # convert the face into grayscale 
            grayscaled_face = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

            smiles = smile_detector.detectMultiScale(grayscaled_face, scaleFactor=1.7, minNeighbors=30)

            # Label the face as smiling 
            if len(smiles) > 0:
                cv2.putText(frame, "SMILING", (x,y+h+40), fontFace= cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,255,0))

        # display frame
        cv2.imshow("Smile Detector", frame)
        
        # Exit if 'SPACE-BAR' is pressed
        if keyboard.is_pressed(" "):
            break
        else:
            # read next frame every 1 millisecond
            cv2.waitKey(1)
            
# release the webcam after done
webcam.release()
# destroy/close all windows
cv2.destroyAllWindows()

# code ran without errors
print("Code Completed!")