import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "F:/ComputerVision/OpenCVPro/venv/Resources/lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=3)

cv2.imshow("Lena",img)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("BlurScale",imgBlur)
cv2.imshow("CannyScale",imgCanny)
cv2.imshow("DilationScale",imgDilation)
cv2.imshow("ErodeScale",imgEroded)
cv2.waitKey(0)