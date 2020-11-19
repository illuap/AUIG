import cv2
import numpy as np

from src.ImageGrabber.ImageGrabber import ImageGrabber
from src.ImageGrabber.ScreenGrabber import ScreenGrabberWin32

class ImageRecognition():
    """ 
    Combines the DAL modules (Image Grabber, Screen Grabber) to help do some pygui/CV2 comparisons
    in helping make decisions.

    """ 
    imageGrabber = None
    screenGrabber = None


    def __init__(self, appName = "NoxPlayer"):
        # used for accessing local image files.
        self.imageGrabber = ImageGrabber()

        # used for accessing an application view.
        self.screenGrabber = ScreenGrabberWin32(appName) # can add support for other OS's in the future.


    # https://stackoverflow.com/questions/58158129/understanding-and-evaluating-template-matching-methods

    # Multiple Objects https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html

    def _findSubImage_try_1_bestmatch_pos(self, large_img, small_img):
        """ 
        Get top-left coordinate of the best matched image if there are any.
        will convert the images into grey if they aren't already 
        """
        large_img_gray = cv2.cvtColor(large_img, cv2.COLOR_BGR2GRAY)
        small_img_gray = cv2.cvtColor(small_img, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(large_img_gray, small_img_gray, cv2.TM_CCOEFF_NORMED)  

        threshold = 0.8
        loc = np.where(result == np.max(result)) # Get the best one
        loc2 = np.where(result >= threshold) # Check threshholds

        if(len(loc2[0]) > 0):
            return (loc[1][0], loc[0][0])
        else:
            return None

    def findSubImagePosInApplication(self, imagePathToFind):
        appImg = self.screenGrabber.getScreenShotRGB()
        findImg = self.imageGrabber.grabImageFromFile(imagePathToFind)

        results = self._findSubImage_try_1_bestmatch_pos(appImg, findImg)

        if results == None:
            return None

        return results

    def findSubImagePosInApplication_show(self, imagePathToFind):
        """ Try to find an image in the application and return it highlighted """
        appImg = self.screenGrabber.getScreenShotRGB()
        findImg = self.imageGrabber.grabImageFromFile(imagePathToFind)

        results = self._findSubImage_try_1_bestmatch_pos(appImg, findImg)

        if results == None:
            print("Failed to find " + imagePathToFind)
            return np.ascontiguousarray(appImg)

        # Draw the rectangle
        MPx,MPy = results
        trows,tcols = findImg.shape[:2]

        newAppImg = np.ascontiguousarray(appImg)

        cv2.rectangle(newAppImg, (int(MPx), int(MPy)),(int(MPx+tcols), int(MPy+trows)),(0,0,255),2)

        return newAppImg

        