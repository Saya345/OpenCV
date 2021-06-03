import cv2
print("Package Imported")
# how to read image videos and webcam

#imges
img = cv2.imread("F:\pythonProject\Resource\lena.jpg")
cv2.imshow('OutPut', img)
# 需要延迟
cv2.waitKey(0) #代表无限延迟  1代表1毫秒 1000=1s


#videos
cap = cv2.VideoCapture("Resource/test_video.mp4")
#需要读取每一帧，添加while循环
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #ord():返回ASCII码的数值
        break

#webcam
#写入摄像机的ID，0为默认的摄像头
cap = cv2.VideoCapture(0)

#定义一些参数,具有特定大小
cap.set(3,640) #cap.set(ID,height)
cap.set(4,480) #cap.set(ID,height)

#改变亮度
cap.set(10,100)

#需要读取每一帧，添加while循环
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #ord():返回ASCII码的数值
        break