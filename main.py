from configmanager import config
from screengrabber import ScreenGrabberWin32
from action import *

from enums.actionTypes import actionTypes
from actionProfile import *

print(config['APPNAME'])

aP = actionProfile("test")

SG = ScreenGrabberWin32(config["APPNAME"])
SG.getScreenShot()

temp = findAndClickAct(SG, aP)
temp.run()

#SGManager = ScreenGrabberWin32(config["APPNAME"])
#SGManager.getScreenShot()


