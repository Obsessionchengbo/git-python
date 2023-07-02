# 导入cv模块
import cv2 as cv

# 绘制矩阵和圆形

# 读取图片
img1 = cv.imread('face1.jpg')

# 修改尺寸
resize1 = cv.resize(img1,dsize=(400,600))

# 坐标
x,y,w,h=100,100,100,100

# 绘制矩形
cv.rectangle(resize1,(x,y,x+w,x+h),color=(0,0,255),thickness=1)

# 绘制圆形
cv.circle(resize1,center=(x+w,y+h),radius=100,color=(0,255,0),thickness=2)

# 显示
cv.imshow('face1_img',resize1)

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()