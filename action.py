from abc import ABC
import uuid 
from enum import Enum
from PIL import Image
import numpy as np
import cv2
import pyautogui
import random

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
        mainImg = self.screenGrabber.getScreenShotRGB()
        gray = cv2.cvtColor(mainImg, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray, self.img1, cv2.TM_CCOEFF_NORMED)  
        
        found_pos = np.unravel_index(result.argmax(),result.shape)
        print (found_pos)

        clickAtPos(self.screenGrabber, found_pos[1], found_pos[0])



    # storage of all the existing profiles in the actions.json