
import cv2
import numpy as np

# create an overlay image. You can use any image
background = np.ones((100,100,3),dtype='uint8')*255
# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.4
while True:
    # read the frame
    ret, frame = cap.read()
    # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
    added_image = cv2.addWeighted(frame[150:250,150:250,:],alpha,background[0:100,0:100,:],1-alpha,0)
    # Change the region with the result
    frame[150:250,150:250] = added_image
    # For displaying current value of alpha(weights)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('a',frame)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0
# Release the camera and destroy all windows         
cap.release()
cv2.destroyAllWindows()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
import cv2
import numpy as np
 
# create an overlay image. You can use any image
background = np.ones((100,100,3),dtype='uint8')*255
# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.4
while True:
    # read the frame
    ret, frame = cap.read()
    # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
    added_image = cv2.addWeighted(frame[150:250,150:250,:],alpha,background[0:100,0:100,:],1-alpha,0)
    # Change the region with the result
    frame[150:250,150:250] = added_image
    # For displaying current value of alpha(weights)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'alpha:{}'.format(alpha),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('a',frame)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break
    # press a to increase alpha by 0.1
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    # press d to decrease alpha by 0.1
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0
# Release the camera and destroy all windows         
cap.release()
cv2.destroyAllWindows()