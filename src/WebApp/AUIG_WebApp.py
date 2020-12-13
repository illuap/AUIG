import eel

from src.ActionNetwork.ActionNetwork import ActionNetwork
from src.Actions.ActionProfileManager import ActionProfileManager
from src.WebApp.EelAPI import *

class AUIRG_WebApp(object):
    __instance__ = None

    apManager: ActionProfileManager = None
    aNetwork: ActionNetwork = None

    def __init__(self):

        if AUIRG_WebApp.__instance__ is None:
            AUIRG_WebApp.__instance__ = self
            self.apManager = ActionProfileManager()
            self.aNetwork = ActionNetwork(self.apManager)
            print("initializing webapp for the first time!")
        else:
            raise Exception("you cannot create another AUIRG_WebApp (bc its a singleton use getinstance())")
        
    def get_instance():
        if not AUIRG_WebApp.__instance__:
            AUIRG_WebApp()
        return AUIRG_WebApp.__instance__



        # TODO start up all the managers and such??
        # this creates a singleton interms of how everything will be managed..
        # but this should be fine for our specific use case because it shouldn't
        # scale that large.....????

