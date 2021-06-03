#检测图像中的形状；勾勒出拐角的轮廓；
#三角形、圆形、矩形、正方形，并将其分类
#最终目标，显示它属于哪个类别，具体有多少个拐点，每个形状的面积

#预处理：将原始图像转化为灰度图像——有利于找到边缘——找到拐角点
import cv2
import numpy as np

#堆叠函数
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    # & 输出一个 rows * cols 的矩阵（imgArray）
    print(rows,cols)
    # & 判断imgArray[0] 是不是一个list
    rowsAvailable = isinstance(imgArray[0], list)
    # & imgArray[][] 是什么意思呢？
    # & imgArray[0][0]就是指[0,0]的那个图片（我们把图片集分为二维矩阵，第一行、第一列的那个就是第一个图片）
    # & 而shape[1]就是width，shape[0]是height，shape[2]是
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    # & 例如，我们可以展示一下是什么含义
    cv2.imshow("img", imgArray[0][1])

    if rowsAvailable:
        for x in range (0, rows):
            for y in range(0, cols):
                # & 判断图像与后面那个图像的形状是否一致，若一致则进行等比例放缩；否则，先resize为一致，后进行放缩
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # & 如果是灰度图，则变成RGB图像（为了弄成一样的图像）
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # & 设置零矩阵
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    # & 如果不是一组照片，则仅仅进行放缩 or 灰度转化为RGB
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#定义一个函数 ————getcontours(获得边缘的函数)
def getContours(img):
    #使用查找轮廓的函数对轮廓进行查找：
    # retrieve method #第2个参数为检索极端的外部轮廓————可以寻找好的外部细节和拐角
    # 点的chain相当于0
    #如果检测出边缘，则在contours里面
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #不止一条
    for cnt in contours:
        #找到区域
        area = cv2.contourArea(cnt)
        #print(area)
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)  #-1表示画所有的框
        #绘制
        if area >500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)  # -1表示画所有的框
        #计算曲线的长度周长（perimeter）
        peri = cv2.arcLength(cnt,True)
        #print(peri)
        #计算有多少的拐角点
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        #print(approx)
        # print(len(approx))
        #创建对象角，得出边界框
        objCor = len(approx)
        x,y,w,h = cv2.boundingRect(approx)

        if objCor == 3:
            objectType = "Tri"
        elif objCor == 4:
            aspRatio = w/float(h)
            if aspRatio>0.95 and aspRatio<1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif objCor > 4:
            objectType ="Circles"
        else:
            objectType = "None"
        #画出boundingbox的函数
        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #标注~~
        cv2.putText(imgContour, objectType, (x + (w // 2) - 10, y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.2,
                        (0, 0, 0), 1)  #字体、范围、颜色、thick =2


path = "F:\pythonProject\Resource\shapes.png"
img = cv2.imread(path)
#复制原始图像
imgContour = img.copy()
#空白的黑色图片
imgBlank = np.zeros_like(img)
#灰度图
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#模糊
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
#检测边缘————边缘检测器Canny
imgCanny = cv2.Canny(imgBlur,50,50)   #50为阈值

getContours(imgCanny)


imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stacked Image",imgStack)
cv2.waitKey(0)
