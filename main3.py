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
        locations = np.where(result >= threshold)
        print(type(locations))
        locations = list(zip(*locations[::-1]))
        print(locations)


        if locations:
            height = self.temping.shape[0]
            width = self.temping.shape[1]
            
            for loc in locations:
                bottomright = (loc[0]+width,loc[1]+height)
                cv.rectangle(self.mainimg,loc,bottomright,color=(255,0,255),thickness=2,lineType=cv.LINE_4)
            cv.imshow("result",self.mainimg)
            cv.waitKey()
            cv.destroyAllWindows()


mybot = Classbot('img/newmain.jpg','img/newtemp.jpg')
mybot.search()