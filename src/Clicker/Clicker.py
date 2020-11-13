import pyautogui


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
    def click_at(pos):
        """
        Take over computer input and click a specific coordinate
        """
        enableClickWithSlightRandom = True
        
        if(enableClickWithSlightRandom):
            _click_at_with_random(pos[0], pos[1])
        else:
            pyautogui.leftClick(pos[0], pos[1])
        

