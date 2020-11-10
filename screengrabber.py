from abc import ABC
from configmanager import config
import win32gui, win32com.client
import win32ui
import win32con

import math
from PIL import Image
import numpy as np

# TODO: future support for linux and maybe macs
class ScreenGrabber(ABC):

    # Grab the window to 'listen' to.
    def __init__(self, winName): 
        pass

    def getScreenShot(self):
        pass

### WIN32 ###

class ScreenGrabberWin32(ScreenGrabber):
    
    old_img = None # might bde just used for specific purposes
    cur_img = None

    hwnd = None
    
    x = None
    y = None
    w = None
    h = None
    def __init__(self, winName): 

        # TODO: Do a check for duplicate names/ windows with the same name
        try:
            print("- Trying to find window name: " + winName )
            # this finds a window with a SIMILAR or EXACT name
            self.hwnd = win32gui.FindWindow(None, winName)
            print("- Is window visible: " + str(win32gui.IsWindowVisible(self.hwnd)))
            
            

            if(self.hwnd == 0):
                print("[ERROR] Could not find " + winName)
                exit()
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(self.hwnd)

        except Exception as ex:
            print('[ERROR] calling win32gui.FindWindow ' + str(ex))
            print(' - TRY RUNNING IN ADMIN')
            raise
    
    def getScreenShot(self):
        # https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows

        if(config['FOCUS_ON_EVERY_ACTION'] == 1):
            win32gui.SetForegroundWindow(self.hwnd)
        
        rect = win32gui.GetWindowRect(self.hwnd) # Maybe take this out to optimize performance at the cost of not being able to resize while the app is running
        self.x = rect[0]
        self.y = rect[1]
        self.w = (rect[2] - self.x)
        self.h = (rect[3] - self.y)
        #print(rect)


        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)
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
        return img[:,:,:3] # Remove alpha channel....
        






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
        img.shape = ( bmpinfo['bmHeight'],bmpinfo['bmWidth'],4) # if possible figure out how to ignore alpha channel in conversion
        return img
    

    #TODO idk where this goes...., this doesnt need to be a member function....
    def saveImage(self, img, url = './web/images-screens/'):
        fileFormat = ".png"
        fileName = "TEST"

        image = Image.fromarray(img)
        image.save(""+url+fileName+fileFormat)
        #TODO FIX THE COLOURS
        return (""+url+fileName+fileFormat)