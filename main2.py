import cv2 as cv
import numpy as np


class Classbot:
    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img, cv.IMREAD_ANYCOLOR)
        self.temping = cv.imread(temp_img, cv.IMREAD_ANYCOLOR)
    def search(self):
        result = cv.matchTemplate(self.mainimg,self.temping,cv.TM_CCOEFF_NORMED)
        min,maxVal,minloc,maxloc = cv.minMaxLoc(result)
        threshold = 0.9
        if maxVal >= threshold:
            topleft = maxloc
            height = self.temping.shape[0]
            width = self.temping.shape[1]
            bottomright = (topleft[0]+ width, topleft[1] + height)
            cv.rectangle(self.mainimg,topleft,bottomright,color=(255,255,0),thickness=3,lineType=cv.LINE_4)
   

            font = cv.FONT_ITALIC
            position = (topleft[0]+25,topleft[1]-8)
            fontsize = 0.8
            color = (136,241,70)
            cv.putText(self.mainimg,"Messi",position,font,fontsize,color,thickness=2)

            cv.imshow("result",self.mainimg)
            cv.waitKey()
            cv.destroyAllWindows()

mybot = Classbot('img/1.jpg','img/temp.JPG')
mybot.search()