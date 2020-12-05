import eel

from src.ActionNetwork.ActionNetwork import ActionNetwork
from src.Actions.ActionProfileManager import ActionProfileManager
from src.WebApp.EelAPI import *

class AUIRG_WebApp(object):
    apManager: ActionProfileManager = None
    aNetwork: ActionNetwork = None

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AUIRG_WebApp, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print('')
        self.apManager = ActionProfileManager()
        self.aNetwork = ActionNetwork(self.apManager)


        # TODO start up all the managers and such??
        # this creates a singleton interms of how everything will be managed..
        # but this should be fine for our specific use case because it shouldn't
        # scale that large.....????

