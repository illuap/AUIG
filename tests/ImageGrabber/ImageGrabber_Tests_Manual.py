import unittest
import cv2

from src.ImageGrabber.ImageGrabber import ImageGrabber

class ImageGrabber_Tests_Manual(unittest.TestCase):

    def dog(self):
        return
    # def test_grabNoxImage(self):
    #     ig = ImageGrabber()

    #     img = ig.grabNoxImage()
    #     cv2.imshow('Nox Image', img) #Technically Image previewer does this for me..


    #     #cv2.waitKey(0)
    #     return 



class ImageGrabber_Tests(unittest.TestCase):
    def test_grabImageFromFile_existing(self):
        ig = ImageGrabber()

        imageList = ["images/test/test_image_1.jpg",
                        "images/test/test_image_2.png",
                        "images/test/find_image_1.png"]

        for path in imageList:
            print("Trying to load: " + path)
            self.assertIsNotNone(ig.grabImageFromFile(path))