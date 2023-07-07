import cv2 as cv
import numpy as np


class Classbot:

    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img, cv.IMREAD_ANYCOLOR)
        self.temping = cv.imread(temp_img, cv.IMREAD_ANYCOLOR)

    def search(self,threshold = 0.9, debug=False ):
        result = cv.matchTemplate(self.mainimg,self.temping,cv.TM_CCOEFF_NORMED)
        min,maxVal,minloc,maxloc = cv.minMaxLoc(result)
        threshold = 0.9
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        height = self.temping.shape[0]
        width = self.temping.shape[1]
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]),width,height]
            rectangles.append(rect)
            rectangles.append(rect)
        point = []
        rectangles,_ = cv.groupRectangles(rectangles,groupThreshold=1,eps=0.5)
        if len(rectangles):
            # print(len(rectangles))
            for (x,y,w,h) in rectangles:
                topleft = (x,y)
                bottomright = (x+w,y+h) 
                centerzx = x + int(w / 2)
                centerzy = y + int( h / 2)
                point.append((centerzx,centerzy))
                if debug:
                    cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2,lineType=cv.LINE_8) 
                    # print(centerzx,centerzy)
                    cv.drawMarker(self.mainimg,(centerzx,centerzy),color=(0,255,1),thickness=2,markerSize=30,markerType=cv.MARKER_CROSS)
        else:
            print("Not image")
        if debug:
            print(f"เจอรูปภาพทั้งหมด = {len(rectangles)}")
            print(point)
            cv.imshow("result",self.mainimg)
            cv.waitKey()
            cv.destroyAllWindows()
        return point
        exit 

mybot = Classbot('img/newmain.jpg','img/newtemp.jpg')
mypoint = mybot.search(debug=True)
print(mypoint)

