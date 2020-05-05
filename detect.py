import yolo
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import glob
import cv2
import sys
import sort

def detect_img(yolo, length, image, path):
    for i in range(length):
        try:
            img = Image.open(path[i])
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(img, image[i])
            # cv2.imwrite("images/"+image[i], np.asarray(r_image)[..., ::-1])
    yolo.yolo.close_session()


def sample(length, image):
    for i in range(length):
        print(image[i])


if __name__ == '__main__':
    image, path = hoge.sort()
    length = len(image)
    detect_img(yolo.YOLO(), length, image, path)
