from abc import ABC

from loguru import logger

from configmanager import config
import win32gui, win32com.client
import win32ui
import win32con

import math
from PIL import Image
import numpy as np


# This is to handle the lowlevel stuff.


# TODO: future support for linux and maybe macs
class ScreenGrabber(ABC):

    # Grab the window to 'listen' to.
    def __init__(self, winName):
        pass

    def getScreenShot(self):
        pass


### WIN32 ###

class ScreenGrabberWin32(ScreenGrabber):
    old_img = None  # might bde just used for specific purposes
    cur_img = None

    hwnd = None

    x: int = None
    y: int = None
    w: int = None
    h: int = None

    def __init__(self, winName):

        # TODO: Do a check for duplicate names/ windows with the same name
        try:
            # this finds a window with a SIMILAR or EXACT name
            self.hwnd = self.findWindowHWD(winName)

            if self.hwnd == 0:
                logger.error("[ERROR] Could not find " + winName)
            # self.setWindowToForeground()

        except Exception as ex:
            logger.trace(ex)
            logger.error('[ERROR] calling win32gui.FindWindow ' + str(ex))
            logger.error(' - TRY RUNNING IN ADMIN')
            raise ex

    def findWindowHWD(self, windowName):
        return win32gui.FindWindow(None, windowName)

    def isWindowVisible(self):
        return win32gui.IsWindowVisible(self.hwnd)

    def setWindowToForeground(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.ShowWindow(self.hwnd, 9)  # 9 is restore.
        win32gui.SetForegroundWindow(self.hwnd)

    def getWindowPosition(self) -> (int, int):
        rect = win32gui.GetWindowRect(
            self.hwnd)  # Maybe take this out to optimize performance at the cost of not being able to resize while the app is running
        self.x = rect[0]
        self.y = rect[1]
        self.w = (rect[2] - self.x)
        self.h = (rect[3] - self.y)
        return self.x, self.y

    def getScreenShot(self):
        # https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows

        if (config['FOCUS_ON_EVERY_ACTION'] == 1):
            self.setWindowToForeground()

        rect = win32gui.GetWindowRect(
            self.hwnd)  # Maybe take this out to optimize performance at the cost of not being able to resize while the app is running
        self.x = rect[0]
        self.y = rect[1]
        self.w = (rect[2] - self.x)
        self.h = (rect[3] - self.y)
        # print(rect)

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, "wut.bmp")

        img = self.__convertWinBitMapToRGBA(dataBitMap)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img

    def getScreenShotRGB(self):
        img = self.getScreenShot()
        return img[:, :, :3]  # Remove alpha channel....

    # Not really used because we will be using CV2 Rather then pyautogui for image detection!!~
    def __convertWinBitMapToPIL(self, dataBitMap):
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        return im

    def __convertWinBitMapToRGBA(self, dataBitMap):
        bmpinfo = dataBitMap.GetInfo()
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (
        bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)  # if possible figure out how to ignore alpha channel in conversion
        return img

    def __convertWinBitMapToCV2Image(self, dataBitMap):
        signedIntsArray = dataBitMap.GetBitmapBits(False)
        img = np.array(signedIntsArray).astype(dtype="uint8")
        return img

    # TODO idk where this goes...., this doesnt need to be a member function....
    def saveImage(self, img, url='./web/images-screens/'):
        fileFormat = ".png"
        fileName = "TEST"

        image = Image.fromarray(img)
        image.save("" + url + fileName + fileFormat)
        # TODO FIX THE COLOURS
        return ("" + url + fileName + fileFormat)
