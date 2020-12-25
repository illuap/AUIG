from random import randint

import pyautogui

from src.ImageGrabber.ScreenGrabber import ScreenGrabberWin32

class Clicker():
    
    @staticmethod
    def _click_at_with_random(x_offset, y_offset):
        min_rand = 1
        max_rand = 10
        randx = randint(min_rand, max_rand)
        randy = randint(min_rand, max_rand)

        pyautogui.leftClick(x_offset + randx,
                            y_offset + randy)

    @staticmethod
    def click_at(pos, offset_pos=(0,0)):
        """
        Take over computer input and click a specific coordinate
        """
        enable_click_with_slight_random = True

        new_pos = (pos[0]-offset_pos[0], pos[1]-offset_pos[1])

        if enable_click_with_slight_random:
            Clicker._click_at_with_random(new_pos[0], new_pos[1])
        else:
            pyautogui.leftClick(new_pos[0], new_pos[1])
        
    @staticmethod
    def click_at_in_app(pos):
        sg = ScreenGrabberWin32("NoxPlayer") # TODO fix this, kinda ugly to instantiate a new class
        Clicker.click_at(pos, sg.getWindowPosition())

