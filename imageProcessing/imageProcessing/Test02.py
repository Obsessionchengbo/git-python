# 导入cv模块
import cv2 as cv

# 读取图片
img1 = cv.imread('face1.jpg')
img2 = cv.imread('face2.png')

# 灰度转换
gray_img1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

# 显示图片
cv.imshow('read_img1',gray_img1)
cv.imshow('read_img2',gray_img2)

# 保存图片
cv.imwrite('gray_face11.jpg',gray_img1)
cv.imwrite('gray_face21.png',gray_img2)

# 等待
cv.waitKey(0)

# 释放内存
cv.destroyAllWindows()