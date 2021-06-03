import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)  # 像素值范围0-255  zeros代表像素为黑色

# 为图像添加色彩
# img[:] = 255,0,0  #为整张蓝色
# img[0:50,40:500] = 255,0,0   # 局部变为蓝色

# 创建线条

cv2.line(img, (0, 0), (100, 100), (0, 255, 0), 3)  # (图像，起点，终点，颜色，厚度)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (5, 55, 0), 3)

# 创建矩形
cv2.rectangle(img, (0, 0), (300, 250), (0, 0, 255), 2)
cv2.rectangle(img, (0, 0), (300, 250), (0, 0, 255), cv2.FILLED)  # 将矩形填满

# 创建圆圈
cv2.circle(img, (250, 250), 50, (0, 150, 150), 2)

# 创建文本
cv2.putText(img, "You are a pig!", (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
