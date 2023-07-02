# 导入cv模块
import cv2 as cv

# 读取图片
img1 = cv.imread('face1.jpg')
img2 = cv.imread('face2.png')

# 显示图片
cv.imshow('read_img1',img1)
cv.imshow('read_img2',img2)
# 等待
cv.waitKey(0)

# 释放内存
cv.destroyAllWindows()