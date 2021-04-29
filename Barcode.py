import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

def decode(img):
  
    decoded_data = pyzbar.decode(img)

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

def HPF(img):
    
    fil = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

    sharp = cv2.filter2D(img, -1, fil)

    return sharp

def thresholding(img):
    ret, image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    return image



image = cv2.imread("H:\Projects\Barcode\Codes\201783_Red Bull.PNG")

image = pre_processing(image)
cv2.imshow("b1", image)

blur_image = noise_removal(image)
cv2.imshow("b2", blur_image)

sharpend_image = HPF(blur_image)
cv2.imshow("b3", sharpend_image)

final_image = thresholding(blur_image)
cv2.imshow("b4", final_image)

decoded_data = decode(final_image)
print(decoded_data)
