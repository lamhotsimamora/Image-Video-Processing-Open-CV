# Developed by @lamhotsimamora
# Powered by Open CV
# Copyright@2018
# lamhotsimamora36@gmail.com

from tkinter import filedialog
from matplotlib import pyplot as plt
import cv2,tkinter as tk,numpy as np

def cannyEdge():
	file  = openFile()
	check = file.lower()
	if check.endswith('.jpg') or check.endswith('.png'):
		img   = cv2.imread(file,0)
		edges = cv2.Canny(img,100,200)
		plt.subplot(121),plt.imshow(img,cmap = 'gray')
		plt.title('Original Image'), plt.xticks([]), plt.yticks([])
		plt.subplot(122),plt.imshow(edges,cmap = 'gray')
		plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
		plt.show()
	else:
		input('The file is not image')

def histogram():
	file  = openFile()
	check = file.lower()
	if check.endswith('.jpg') or check.endswith('.png'):
		img = cv2.imread(file)
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
		plt.imshow(hist,interpolation = 'nearest')
		plt.show()
	else:
		input('The file is not image')

def gradient():
	file  = openFile()
	check = file.lower()
	if check.endswith('.jpg') or check.endswith('.png'):
		img = cv2.imread(file,0)
		laplacian = cv2.Laplacian(img,cv2.CV_64F)
		sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
		sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
		plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
		plt.title('Original'), plt.xticks([]), plt.yticks([])
		plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
		plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
		plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
		plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
		plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
		plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
		plt.show()
	else:
		input('The file is not image')


def opticalFlow():
	file  = openFile()
	check = file.lower()
	if check.endswith('.mkv') or check.endswith('.flv') or check.endswith('.mp4'):
		cap = cv2.VideoCapture(file)
		ret, frame1 = cap.read()
		prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
		hsv = np.zeros_like(frame1)
		hsv[...,1] = 255
		while(1):
		    ret, frame2 = cap.read()
		    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
		    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
		    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
		    hsv[...,0] = ang*180/np.pi/2
		    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
		    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

		    cv2.imshow('frame2',rgb)
		    k = cv2.waitKey(30) & 0xff
		    if k == 27:
		        break
		    elif k == ord('s'):
		        cv2.imwrite('opticalfb.png',frame2)
		        cv2.imwrite('opticalhsv.png',rgb)
		    prvs = next

		cap.release()
		cv2.destroyAllWindows()
	else:
		input('The file is not video')

def blur():
	file  = openFile()
	check = file.lower()
	if check.endswith('.jpg') or check.endswith('.png'):
		img = cv2.imread(file)
		kernel = np.ones((5,5),np.float32)/25
		dst = cv2.filter2D(img,-1,kernel)
		blur = cv2.blur(img,(5,5))
		plt.subplot(121),plt.imshow(img),plt.title('Original')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
		plt.xticks([]), plt.yticks([])
		plt.show()
	else:
		input('The file is not image')

def tresholding():
	file= openFile()
	check = file.lower()
	if check.endswith('.jpg') or check.endswith('.png'):
		img = cv2.imread(file,0)
		img = cv2.medianBlur(img,5)

		ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
		th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
		            cv2.THRESH_BINARY,11,2)
		th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		            cv2.THRESH_BINARY,11,2)

		titles = ['Original Image', 'Global Thresholding (v = 127)',
		            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
		images = [img, th1, th2, th3]

		for i in range(4):
		    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
		    plt.title(titles[i])
		    plt.xticks([]),plt.yticks([])
		plt.show()
	else:
		input('The file is not image')

def openFile():
	dir = tk.Tk()
	dir.withdraw()
	return filedialog.askopenfilename()





