import cv2
import numpy as np

#OpenCV x轴方向为东 ，y轴方向为南（与现实中画x,y（北）轴）不一样；


#原图像大小
img = cv2.imread("F:\pythonProject\Resource\mingren.jpeg")
print(img.shape)

#调整图像大小
imgResize = cv2.resize(img,(200,300))
print(imgResize.shape)

#裁剪图像大小
imgCropped = img[0:200,0:50]  #0:200（长）,0:50（宽）


#裁剪图像（使用到矩阵功能）

cv2.imshow("Image",img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)

