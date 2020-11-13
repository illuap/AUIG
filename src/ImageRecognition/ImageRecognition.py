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


    def findSubImageInApplication(self, imagePathToFind):
        # pygui find image?

        appImg = self.screenGrabber.getScreenShotRGB()
        findImg = self.imageGrabber.grabImageFromFile(imagePathToFind)

        method = cv2.TM_CCOEFF_NORMED

        result = cv2.matchTemplate(findImg, appImg, method)
        print(result)
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)
        MPx,MPy = mnLoc
        trows,tcols = findImg.shape[:2]

        newAppImg = np.ascontiguousarray(appImg)
        # Step 3: Draw the rectangle on large_image
        cv2.rectangle(newAppImg, (int(MPx), int(MPy)),(int(MPx+tcols), int(MPy+trows)),(0,0,255),2)

        # Display the original image with the rectangle around the match.
        cv2.imshow('output',newAppImg)

        # The image is only displayed if we call this
        cv2.waitKey(0)

        return

    def findSubImageInApplication_show(self, imagePathToFind):
        # pygui find image?

        appImg = self.screenGrabber.getScreenShotRGB()
        findImg = self.imageGrabber.grabImageFromFile(imagePathToFind)

        method = cv2.TM_SQDIFF_NORMED

        result = cv2.matchTemplate(findImg, appImg, method)
        print(result)
        mn,_,mnLoc,_ = cv2.minMaxLoc(result)
        MPx,MPy = mnLoc
        trows,tcols = findImg.shape[:2]

        newAppImg = np.ascontiguousarray(appImg)
        # Step 3: Draw the rectangle on large_image
        cv2.rectangle(newAppImg, (int(MPx), int(MPy)),(int(MPx+tcols), int(MPy+trows)),(0,0,255),2)

        # Display the original image with the rectangle around the match.
        cv2.imshow('output',newAppImg)

        # The image is only displayed if we call this
        cv2.waitKey(0)

        return





        # Specify a threshold 
        threshold = 0.8
        # Store the coordinates of matched area in a numpy array 
        loc = np.where( result >= threshold)  
        if(config["DEBUG_IMAGES"] == 1):
            print(loc)
            # Draw a rectangle around the matched region. 
            for pt in zip(*loc[::-1]): 
                cv2.rectangle(gray, pt, (pt[0] + 20, pt[1] + 20), 255, 1) 
            
            # Show the final image with the matched area. 
            cv2.imshow('Detected',gray) 
            cv2.waitKey(0)


        if(len(loc[0]) > 0):
            clickAtPos(self.screenGrabber, loc[1][0], loc[0][0])
            return actionStatusTypes.ACTION_DONE
        else:
            return actionStatusTypes.NO_ACTION