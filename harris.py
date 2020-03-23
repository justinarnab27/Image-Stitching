import numpy as np
import cv2

def harris(img):
	w = np.ones((3,3))
	return w


img = cv2.imread("mountain.jpg",1)
cv2.namedWindow("win",cv2.WINDOW_NORMAL)
cv2.imshow("win",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(harris(img))