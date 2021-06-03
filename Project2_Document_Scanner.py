import cv2
import numpy as np

#####################################################
WidthImg = 640
HeightImg = 480
#####################################################
# 引入webcam
cap = cv2.VideoCapture(0)
cap.set(3,WidthImg)
cap.set(4,HeightImg)
cap.set(10,130) #亮度


def prePossessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    #做膨胀和侵蚀的好处为：易于检测
    kernel = np.ones((5,5))
    imgDila = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDila,kernel,iterations=1)
    return imgThres

def getContours(img) -> object:
    biggest = np.array([])
    maxArea = 0
    contours,hierachy = cv2.findContours(imgCount,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>5000:
            # cv2.drawContours(imgCount,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) ==4 :
                biggest = approx
    cv2.drawContours(imgCount, biggest, -1, (255, 0, 0), 20) #20为倍数
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print("add",add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    #print("NewPoints",myPointsNew)
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

def getWarp(img,biggest):
    biggest = reorder(biggest)
    reorder(biggest)
    print(biggest.shape)   4组点，每一个点都包括想x,y
    pts1 = np.float32(biggest)
    pta2 = np.float32([[0,0],[WidthImg,0],[0,HeightImg],[WidthImg,HeightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pta2)
    imgOutput = cv2.warpPerspective(img,matrix,(WidthImg,HeightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(WidthImg,HeightImg))

    return imgCropped

while True:
    success, img = cap.read()
    cv2.resize(img,WidthImg,HeightImg)
    imgCount = img.copy()

    imgThres = prePossessing(img)
    biggest = getContours(imgThres)
    #print(biggest)

    if biggest!=0:
        imgWarpped = getWarp(img,biggest)
        imageArray = ([img,imgThres],
                  [imgCount,imgWarpped])
    else:
        imageArray = ([img, imgThres],
                      [img, img])

    stackdImges = stackdImges(0.6,imageArray)


    cv2.show("Result",stackdImges)
    cv2.shoe("ImageWarpped",imgWarpped)
    #按q结束循环
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

