import numpy as np
import cv2 as cv
import argparse
from os import listdir
import os
import scipy as sp
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--folder")
parser.add_argument("--outfolder")
args = parser.parse_args()

def crop_bottom_half(image):
    x1=image.shape[0]*4/9 #Most information regarding output variables retained in above half of the image
    x2=image.shape[0]
    y2=image.shape[1]
    cropped_img = image[0:int(x1),0:int(y2)]
    return cropped_img
    
for filename in listdir(args.folder):
    img = cv.imread(str(args.folder)+'/'+filename)
    print(str(args.folder))
    cropimg = crop_bottom_half(img)
    cropped = cv.GaussianBlur(cropimg, (5,5),0)
    gray = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU )
    kernel = np.ones((5,5),np.uint8)
    closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
    edges = cv.Canny(closing,100,200)
    cv.imwrite(os.path.join(args.outfolder , filename), edges)