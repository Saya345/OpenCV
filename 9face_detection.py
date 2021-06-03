#opencv提供了级联的文件（可以自定义级联）
import cv2



#添加级联文件（Positives Faces 和 Negatives Non Faces 同时进行训练————最终生成XML File【级联文件哟】）
faceCascade = cv2.CascadeClassifier("F:\pythonProject\Learn-OpenCV-in-3-hours-master\Resources\haarcascade_frontalface_default.xml")
img = cv2.imread("F:\pythonProject\Learn-OpenCV-in-3-hours-master\Resources\lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#对脸进行级联点检测
faces = faceCascade.detectMultiScale(imgGray,1.1,4)  #1.1为比例因子，最小的值为4

#创建边界框
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)