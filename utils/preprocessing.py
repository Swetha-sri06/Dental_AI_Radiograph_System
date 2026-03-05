# image preprocessing functions
import cv2
import numpy as np

def preprocess_image(img_path):

    img = cv2.imread(img_path,0)
    img = cv2.resize(img,(512,512))

    img = cv2.equalizeHist(img)

    img = img/255.0

    return np.expand_dims(img,axis=0)
