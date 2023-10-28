from pyfiglet import Figlet
from cv2 import imshow, waitKey, cvtColor, COLOR_RGB2GRAY, IMREAD_GRAYSCALE
import matplotlib.pyplot as plt
import sys
import cv2

# initialize work_with_image object
figlet = Figlet()

def main():
    image_path = "C:/Users/DELL E3390/Pictures/screensaver/spa.jpg"
    image = read_image(image_path)
    image_gray = read_img_in_grayFormat(image_path)

    if image is None:
        sys.exit("Image is not successfully uploaded")

    if image_gray is None:
        sys.exit("Image is not successfully uploaded")

    # print(f"Dimension: {image.shape}, \nDatatype: {image.dtype}")
    # print(f"{image[0, 0: 500]}")
    # invoke show_image() function
    show_image(image_gray)
    # change_img_color(image)

def read_image(img_path):
    return cv2.imread(img_path)

def show_image(img):
    plt.title("Display SPa's image using matplotlib")
    plt.imshow(img)
    plt.show()
    # === using opencv ===
    imshow("Displaying SPa's image using OpenCV", img)
    waitKey(0)

def change_img_color(img_rgb):
    img_gray = cvtColor(img_rgb, COLOR_RGB2GRAY)
    # side effect
    print(f"{img_gray[0, 0]}")
    plt.imshow(img_gray)
    plt.title("Display SPa's ): Image")
    plt.show()

def read_img_in_grayFormat(img_path):
    return cv2.imread(img_path, IMREAD_GRAYSCALE)

if __name__=="__main__":
    main()
