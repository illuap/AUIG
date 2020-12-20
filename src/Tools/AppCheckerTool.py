
from src.ImageGrabber.ScreenGrabber import ScreenGrabber, ScreenGrabberWin32


class AppCheckerTool():


    @staticmethod
    def DetectNox():
        """ Returns T or F depending if we could detect nox open """
        SG = ScreenGrabberWin32("NoxPlayer")
        return SG.isWindowVisible()

    @staticmethod
    def FocusNox():
        """ Focuses Nox """ 
        SG = ScreenGrabberWin32("NoxPlayer")
        SG.setWindowToForeground()
