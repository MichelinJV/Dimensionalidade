import cv2
from skimage import color

img = cv2.imread('ff.jpg', 2) 

#binarização  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
  
cv2.imshow("Binary", bw_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

#Tons de cinza
imgGray = color.rgb2gray(img)