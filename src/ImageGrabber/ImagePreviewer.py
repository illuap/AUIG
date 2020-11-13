
import os
import cv2
import uuid 

from PIL import Image 



# should i just make this static?

# TODO
class ImagePreviewer(object):

    def openImageFromArr(self, imgArr):
        """ Using CV2 to open and preview images """
        print(imgArr)
        cv2.imshow('image-'+str(uuid.uuid1()),imgArr)
        return

    def openImageFromFile(self, fileName):
        """ Using CV2 to open and preview images """
        image = cv2.imread(fileName, cv2.IMREAD_COLOR)
        cv2.imshow('image-'+str(uuid.uuid1()) ,image)
        return

    def openSelectableSubImage(self):
        return