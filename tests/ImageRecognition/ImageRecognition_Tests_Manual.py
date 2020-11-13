import unittest
import cv2

from src.ImageRecognition.ImageRecognition import ImageRecognition

class ImageRecognition_Tests_Manual(unittest.TestCase):


    def test_findSubImageInApplication(self):
        ir = ImageRecognition() # TODO Make a stub for this.
        imgPathToFind = "images/test/find_image_1.png"


        img = ir.findSubImageInApplication(imgPathToFind)
        #cv2.imshow('Nox Image', img) #Technically Image previewer does this for me..


        cv2.waitKey(0)
        return 