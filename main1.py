import cv2 as cv
import numpy as np


main_img = cv.imread("img/1.jpg", cv.IMREAD_ANYCOLOR)
temp_img = cv.imread("img/temp.JPG", cv.IMREAD_ANYCOLOR)


result = cv.matchTemplate(main_img,temp_img,cv.TM_CCOEFF_NORMED)
min,maxVal,minloc,maxloc = cv.minMaxLoc(result)

threshold = 0.9
if maxVal >= threshold:
    topleft = maxloc
    height = temp_img.shape[0]
    width = temp_img.shape[1]
    bottomright = (topleft[0]+ width, topleft[1] + height)
    cv.rectangle(main_img,topleft,bottomright,color=(255,255,0),thickness=3,lineType=cv.LINE_4)
   

    font = cv.FONT_ITALIC
    position = (topleft[0]+25,topleft[1]-8)
    fontsize = 0.8
    color = (136,241,70)
    cv.putText(main_img,"Messi",position,font,fontsize,color,thickness=2)

    cv.imshow("result",main_img)
    cv.waitKey()
    cv.destroyAllWindows()