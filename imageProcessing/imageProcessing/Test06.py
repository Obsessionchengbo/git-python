# 导入cv模块
import cv2 as cv

# 人脸识别

# 检测函数
def face_detect_demo():
    gray = cv.cvtColor(resize1,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('F:\\download\\opencv\\opencv-4.5.2\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gray,1.01,5,0,(10,10),(300,300))
    for x,y,w,h in face:
        cv.rectangle(resize1,(x,y),(x+w,y+h),color=(0,255,0),thickness=1)
    cv.imshow('result',resize1)

# 读取图片
img1 = cv.imread('face3.jpg')


# 修改尺寸
resize1 = cv.resize(img1,dsize=(460,345))
# 检测函数
face_detect_demo()

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()