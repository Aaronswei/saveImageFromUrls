import os
import cv2
import numpy as np

cur_path = os.getcwd()
img_path = os.path.join(cur_path, "img_data")

bad_image = os.path.join(cur_path, 'raw_data__age_college__5SGFUKF.jpg')
bad_mat = cv2.imread(bad_image)

org_file = []

for files in os.listdir(img_path):
    imagename = os.path.join(img_path, files)

    image = cv2.imread(imagename)

    if image is None:
        os.remove(imagename)
    else:
        resize_image = cv2.resize(image, (bad_mat.shape[1], bad_mat.shape[0]))

        check = cv2.subtract(resize_image, bad_mat)
        out=np.any(check)
        if out==False:
            os.remove(imagename)
