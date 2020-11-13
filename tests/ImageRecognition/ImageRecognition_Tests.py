import unittest
import cv2

from src.ImageRecognition.ImageRecognition import ImageRecognition

class ImageRecognition_Tests(unittest.TestCase):


    def test_findSubImagePosInApplication_fail(self):
        ir = ImageRecognition() # TODO Make a stub for this.
        imgPathToFind = "images/test/test_image_1.jpg"


        pos = ir.findSubImagePosInApplication(imgPathToFind)
        
        self.assertIsNone(pos)

    def test_findSubImagePosInApplication_fail(self):
        ir = ImageRecognition() # TODO Make a stub for this.
        imgPathToFind = "images/test/find_image_2.png"


        pos = ir.findSubImagePosInApplication(imgPathToFind)
        
        self.assertIsNotNone(pos)