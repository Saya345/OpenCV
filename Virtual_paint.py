import cv2
import numpy as np
#写入摄像机的ID，0为默认的摄像头
cap = cv2.VideoCapture(1)
frameWidth = 640
frameHeight = 480
#定义一些参数,具有特定大小
cap.set(3,frameWidth) #cap.set(ID,height)
cap.set(4,frameHeight) #cap.set(ID,height)
cap.set(10,150)#改变亮度

#根据颜色选择器函数，选择颜色
myColor = [[5,107,0,19,255,255]#橙色,
           [133,56,0,159,156,255],
           [52,76,0,100,255,255]]

#创建颜色的值
myColorValues = [[51,153,255],    #BGR
                 [255,0,255],
                 [0,255,0]]


myPoints = []    # [x,y,coloId]
# 定义颜色检测的函数
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    #转化为HSV空间，进行颜色选择
    #对所有的颜色进行循环 # myColor[0][0:3] 橙色的前三个数
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #检查是否能正常工作
        #cv2.imshow(str(color[0]),mask)  #此处命名很随意
        x,y = getContours(mask)   #调用获取边缘的函数
        # cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED) 一个点周围画圈的点均为蓝色
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count =+1
    return newPoints
    #想要寻找不止一种颜色————列出表格myColor（颜色的最大值和最小值）

#找边缘
#定义一个函数 ————getcontours(获得边缘的函数)
def getContours(img):
    #使用查找轮廓的函数对轮廓进行查找：
    # retrieve method #第2个参数为检索极端的外部轮廓————可以寻找好的外部细节和拐角
    # 点的chain相当于0
    #如果检测出边缘，则在contours里面
    x,y,w,h = 0,0,0,0 #为了防止返回时不返回值
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #不止一条
    for cnt in contours:
        #找到区域
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)  # -1表示画所有的框
            #计算曲线的长度周长（perimeter）
            peri = cv2.arcLength(cnt,True)
            #计算有多少的拐角点
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        #cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)



#需要读取每一帧，添加while循环
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColor, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    findColor(img,myColor,myColorValues)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #ord():返回ASCII码的数值
        break


