import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

def decode(img):
  
    decoded_data = pyzbar.decode(img)
    cv2.imshow("1", img)
    for obj in decoded_data:
        data = str(obj.data)
  
    data = data[2:-1]
    return data

def pre_processing(img):
    a = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = cv2.resize(a, (256, 256))

    return a

def noise_removal(img):
    median = cv2.medianBlur(img, 3)

    return median

def unsharpmask(img, blur):
    sharp = img + (img - blur) * 100

    return sharp

def thresholding(img):
    ret, image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    return image



image = cv2.imread("H:\Projects\Barcode\Codes\Hrishil.PNG")

           
image = pre_processing(image)
cv2.imshow("q1", image)

blur_image = noise_removal(image)
cv2.imshow("q2", blur_image)

sharpend_image = unsharpmask(image, blur_image)
cv2.imshow("q3", sharpend_image)

final_image = thresholding(sharpend_image)
cv2.imshow("q4", final_image)

decoded_data = decode(final_image)



