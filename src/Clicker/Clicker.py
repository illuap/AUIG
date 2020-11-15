import pyautogui

from src.ImageGrabber.ScreenGrabber import ScreenGrabberWin32

class Clicker():
    
    @staticmethod
    def _click_at_with_random(sg, x_offset, y_offset):
        minRand = 1
        maxRand = 10
        randx = random.randint(minRand, maxRand)
        randy = random.randint(minRand, maxRand)

        pyautogui.leftClick(sg.x + x_offset + randx,
                            sg.y+ y_offset + randy)

    @staticmethod
    def click_at(pos, offset_pos=(0,0)):
        """
        Take over computer input and click a specific coordinate
        """
        enableClickWithSlightRandom = True

        newPos = (pos[0]-offset_pos[0], pos[1]-offset_pos[1])

        if(enableClickWithSlightRandom):
            _click_at_with_random(newPos[0], newPos[1])
        else:
            pyautogui.leftClick(newPos[0], newPos[1])
        
    @staticmethod
    def click_at_in_app(pos):
        sg = ScreenGrabberWin32() # TODO fix this, kinda ugly to instantiate a new class
        click_at(pos, sg.getWindowPosition())

