from matplotlib import pyplot as plt
import cv2
img = cv2.imread('./images/Lena.png',1)
print img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

#grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
