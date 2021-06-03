import cv2
import numpy as np
img = cv2.imread("F:\pythonProject\Resource\pikepai.png")

width, height = 250,350
pts1 = np.float32([[68,129],[165,109],[92,279],[204,253]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#变换矩阵
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#扭曲变形
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)