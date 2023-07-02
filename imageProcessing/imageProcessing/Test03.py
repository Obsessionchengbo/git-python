# 导入cv模块
import cv2 as cv

# 修改尺寸

# 读取图片
img1 = cv.imread('face1.jpg')
img2 = cv.imread('face2.png')

# 修改尺寸
resize1 = cv.resize(img1,dsize=(400,600))
resize2 = cv.resize(img2,dsize=(192,108))

# 显示原图
cv.imshow('face_img1',img1)
cv.imshow('face_img2',img2)

# 显示修改后的
cv.imshow('resize_img1',resize1)
cv.imshow('resize_img2',resize2)

# 打印原图尺寸大小
print('face1未修改尺寸为:',img1.shape)
print('face2未修改尺寸为:',img2.shape)

# 打印修改后尺寸大小
print('face1修改后的尺寸为:',resize1.shape)
print('face2修改后的尺寸为:',resize2.shape)

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()