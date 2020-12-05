import eel

from .EelAPI import *



def startApp():
    eel.init('web')
    eel.start('actionNetwork.html', size=(600, 500))  # Start