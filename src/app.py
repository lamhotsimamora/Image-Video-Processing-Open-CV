# Developed by @lamhotsimamora
# Powered by Open CV
# Copyright@2018
# lamhotsimamora36@gmail.com

import imageProcess as sys,os

def prepare(menu):
	input('[ '+menu+' ] Choose The Image ! ( Press Enter To Continue )') 

def goTresholding():
	prepare('Tresholding')
	sys.tresholding()

def goCannyEdge():
	prepare('Canny Edge')
	sys.cannyEdge()

def goBlur():
	prepare('Blur / Smoothing')
	sys.blur()

def goDenseOpticalFlow():
    input('[ Dense Optical Flow ] Choose The Video ! ( Press Enter Continue | Press Escape to Close The Video )')
    sys.opticalFlow()

def goGradient():
    prepare('Gradient')
    sys.gradient()

def goHistogram():
    prepare('Histogram')
    sys.histogram()

# ==================================================================================================

def _init():
    print("*********************************************************")
    print("===== Image & Video Processing | Powered by Open CV =====")
    print("*********************************************************")
    print("1.  Tresholding        | Image                           ")
    print("2.  Canny Edge         | Image                           ")
    print("3.  Blur               | Image                           ")
    print("4.  Gradient           | Image                           ")
    print("5.  Histogram 2D       | Image                           ")
    print("6.  Dense Optical Flow | Video                           ")
    print("7.  Clear                                                ")
    print("8.  About                                                ")
    print("*********************************************************")


def clear():
    os.system('cls')
    _init()
    showMenu()


def about():
    print(" ")
    print('Developer @lamhotsimamora')
    print('Image & Video Processing Powered by Open CV & Python 3')
    print('https://github.com/lamhotsimamora')
    showMenu()

def showMenu():
    check = True
    print(" ")
    while check:
        menu = input("Select Menu : ")
        try:
            get   = int(menu)
            check = False
            if get ==  1:
               goTresholding()
               showMenu()
               break
            elif get == 2: 
               goCannyEdge()
               showMenu()
               break
            elif get == 3:
               goBlur()
               showMenu()
               break
            elif get == 4:
               goGradient()
               showMenu()
               break
            elif get == 5:
                goHistogram()
                showMenu()
                break
            elif get == 6:
                goDenseOpticalFlow()
                showMenu()
                break
            elif get == 7:
                clear()
                break
            elif get == 8:
                about()
                break
            else:
               showMenu()
        except ValueError:
            check = True
            showMenu() 

_init()
showMenu()

