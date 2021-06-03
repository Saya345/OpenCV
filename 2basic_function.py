import cv2
import numpy as np
img = cv2.imread("F:\pythonProject\Resource\lena.jpg")

kernel = np.ones((5,5), np.uint8) #5*5全为1的矩阵，2^8 =256 像素范围 0-255
#转换为灰度图
#RGB ---- BGR
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#模糊图像
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
#检测边缘
#imgCanny = cv2.Canny(img,100,100)
imgCanny = cv2.Canny(img,150,200)
imgCanny2 = cv2.Canny(img,50,200)
#膨胀
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
#侵蚀
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Canny Image2", imgCanny2)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)