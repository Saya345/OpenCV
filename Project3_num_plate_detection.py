import cv2

########################
WidthImg = 640
HeightImg = 480
faceCascade = cv2.CascadeClassifier
#######################

# 引入webcam
cap = cv2.VideoCapture(0)
cap.set(3,WidthImg)
cap.set(4,HeightImg)
cap.set(10,130) #亮度