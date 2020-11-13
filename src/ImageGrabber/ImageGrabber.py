import cv2

from src.ImageGrabber.ScreenGrabber import ScreenGrabberWin32


class ImageGrabber():

    screenGrabber = None

    # def __init__(self):
    #      self.screenGrabber = NOne


    def grabNoxImage(self):
        """Focus on NOX and grab an SS of NOX"""
        # TODO remove.
        noxScreenGrabber = ScreenGrabberWin32("NoxPlayer")

        return noxScreenGrabber.getScreenShot()

    def grabNoxSubImage(self):
        """Focus on NOX and grab an sub region from a NOX SS"""
        # TODO remove.
        return
    
    def __grabImageFromApplication(self):
        # TODO remove.
        return

    def __focusApplication(self):
        # TODO remove.
        return

    def grabImageFromFile(self, fileName):
        """ Using CV2 to get an image """
        print(fileName)
        image = cv2.imread(fileName, cv2.IMREAD_COLOR)
        return image


    def grabSubImageFromFile(self):
        """Take a pre-existing image and grab a small chunk from it"""
        return


    # WinAPI to focus applications
    # PYGUI to preview image
    # PYGUI to select sub images
    # 