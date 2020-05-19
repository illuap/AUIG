from abc import ABC
import uuid 
from enum import Enum
from PIL import Image
import numpy as np
import cv2
import pyautogui
import random
from configmanager import config
from enums.actionStatusTypes import actionStatusTypes

class action(ABC):

    name = "Base Action"
    version = 0.0

    def __init__(self):
        pass

    # Dunno if i will need this
    def getView(self):
        pass

    def run(self):
        pass

# TODO move this into a helper class
def GetImage(url):
    #TODO pre-open and cache image
    return cv2.imread(url,0) #this is in grey scale

def clickAtPos(sg, x_offset, y_offset):
    minRand = 1
    maxRand = 10
    randx = random.randint(minRand, maxRand)
    randy = random.randint(minRand, maxRand)

    pyautogui.leftClick(sg.x + x_offset + randx,
                         sg.y+ y_offset + randy)

class findAndClickAct(action):

    _actionProfile = None
    _screenGrabber = None

    img1 = None
    # 
    def __init__(self, SG, aP):
        self._actionProfile = aP
        self.img1 = GetImage(self._actionProfile.data["img1"])
        self.screenGrabber = SG

    def getView(self):
        pass

    def run(self):
        print("Running " + self._actionProfile.uniqueName)

        

        mainImg = self.screenGrabber.getScreenShotRGB()
        gray = cv2.cvtColor(mainImg, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray, self.img1, cv2.TM_CCOEFF_NORMED)  
        
        #JUST TAKES THE FIRST POINT FOUND
        #found_pos = np.unravel_index(result.argmax(),result.shape)

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

class checkAndClickAct(action):
    _actionProfile = None
    _screenGrabber = None

    img1 = None
    # 
    def __init__(self, SG, aP):
        self._actionProfile = aP
        self.img1 = GetImage(self._actionProfile.data["img1"])
        self.x1 = self._actionProfile.data["x1"]
        self.y1 = self._actionProfile.data["y1"]
        self.screenGrabber = SG

    def getView(self):
        pass

    def run(self):
        print("Running " + self._actionProfile.uniqueName)
        mainImg = self.screenGrabber.getScreenShotRGB()
        gray = cv2.cvtColor(mainImg, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray, self.img1, cv2.TM_CCOEFF_NORMED)  
        
        #JUST TAKES THE FIRST POINT FOUND
        #found_pos = np.unravel_index(result.argmax(),result.shape)

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
            print(self.x1)
            clickAtPos(self.screenGrabber, self.y1, self.x1)
            return actionStatusTypes.ACTION_DONE
        else:
            return actionStatusTypes.NO_ACTION




    # storage of all the existing profiles in the actions.json