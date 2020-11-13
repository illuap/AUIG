import unittest
import cv2

from src.ImageGrabber.ImagePreviewer import ImagePreviewer

class ImagePreviewer_Tests_Manual(unittest.TestCase):

    def test_openImageFromFile(self):
        """
        docstring
        """
        filePath = r"images\test\test_image_1.jpg"

        ip = ImagePreviewer()
        ip.openImageFromFile(filePath)

        # For testing purposes only
        #cv2.waitKey(0)
        pass
    
    def test_openImageFromArr(self):
        """
        docstring
        """
        filePath = r"images\test\test_image_2.png"
        imageArr = cv2.imread(filePath, cv2.IMREAD_COLOR)

        ip = ImagePreviewer()
        ip.openImageFromArr(imageArr)
        
        # For testing purposes only
        #cv2.waitKey(0)
        pass


    