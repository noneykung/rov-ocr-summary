import cv2 
import numpy as np
from matplotlib import pyplot as plt

img_file = "data/g-ex-1.png"

img = cv2.imread(img_file)

#cv2.imshow("Orgiinal image", img)
#cv2.waitKey(0)

#display funtion
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    height, width = im_data.shape[:2]  # ใช้แค่ 2 ค่า

    #
    figsize = width / float(dpi), height / float(dpi)

    #
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    #
    ax.axis('off')

    #
    ax.imshow(im_data, cmap='gray')

    plt.show()

#img to gray function
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#remove noise from picture funtion
def noise_removal(img):
    kernal = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernal, iterations=1)
    kernal = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernal, iterations=1)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
    img = cv2.medianBlur(img, 3)
    return (img)

#
def thin_font(img):
    img = cv2.bitwise_not(img)
    kernal = np.ones((2, 2),np.uint8) #thin the bold of white 
    img = cv2.erode(img, kernal, iterations=1)
    img = cv2.bitwise_not(img)
    return (img)

#invert the image to gray or black from
inverted_img = cv2.bitwise_not(img)
cv2.imwrite("temp/inverted.png", inverted_img)

#gray image 
gray_img = grayscale(img)
cv2.imwrite("temp/gray.png", gray_img)

#create the black white img to temp
thresh, im_bw = cv2.threshold(gray_img, 115, 255, cv2.THRESH_BINARY)
cv2.imwrite("temp/bw_image.png", im_bw)

#no noise in img created
no_noise = noise_removal(im_bw)
cv2.imwrite("temp/no-noise.png", no_noise)

#
eroded_img = thin_font(no_noise)
cv2.imwrite("temp/erored_img.png", eroded_img)

#Show the image from temp
display("temp/erored_img.png")
