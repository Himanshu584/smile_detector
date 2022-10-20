# smile_detector
To Clone repository use command :- `git clone https://github.com/Himanshu584/smile_detector`

## DEMO VIDEO


https://user-images.githubusercontent.com/70319246/197010279-662f729a-4370-4752-b31d-49edd0dd0422.mp4



This is a simple AI Smile detection algorithm That returns a window and draws rectangle around the faces detected and also returns the word "SMILING" if the face is smiling.
Though it requires proper lightning to detect the performance of the program is considerably good.

To run the program on your device just clone the repository and run the command `python detector.py`.
To close the program , press `SPACE BAR`


## LOGIC
There are 2 haar cascade files used for smile detection algorithm here namely `haarcascade-frontalface-default` and `haarcascade-smile`.
logic is simple that for detection of a smile on a face, the algo first has to detect a face. This was neccessary to improve the accuracy of the algo because by just 
detecting smiles we would introduce a lot of noise into the algorithm due to environment. many things like for example a curtain with certain lightning could resemble the curve like
smile. to reduce this noise we isolate the faces for the smile detection file by using face detection file.

## BUG
There is a small bug that it does not close the program when we hit the close 'X' icon on top of window due to infinite while loop.This was countered by a hack that if
`spacebar` was pressed the loop will break. Any fixes for the same would be appreciated 😀.
