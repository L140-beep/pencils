import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_closing, binary_erosion

count = 0
pencils = 0
for i in range(1, 13):
    count = 0
    image = cv2.imread(f'homework/pencils/images/img ({i}).jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    ret, th = cv2.threshold(blur,0,1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    th[th==1] = 2
    th[th==0] = 1
    th[th==2] = 0

    th = binary_closing(binary_closing(th))
    labeled = label(th)


    regions = regionprops(labeled)
    for region in regions:
        if region.area > 250000:
            if region.equivalent_diameter_area > 550 and region.equivalent_diameter_area < 700:
                count += 1
                pencils += 1
    
    print(f"Изображение {i}: {count}")

print(f"Количество карандашей: {pencils}")