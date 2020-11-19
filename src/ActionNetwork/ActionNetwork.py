import keyboard
import time

from src.Actions.ActionProfileManager import ActionProfileManager
from src.Actions.ActionProfileModel import ActionProfileModel

class ActionNetwork(object):


    APManager = None


    def __init__(self, actionProfileManager: ActionProfileManager):
        self.APManager = actionProfileManager
        # Need screen grabbber
        # Current state
        # how to execute an action
        # how to choose the first action
        # how to 

    def getStartingNode(self):
        return self.APManager.getStartingAction()

    def traverseNetwork(self, startingAction: ActionProfileModel = None):
        if(not startingAction):
            startingAction = self.APManager.getStartingAction()
        # TODO
        while(not keyboard.is_pressed('`') and results != ""):
            nextActionName = self.APManager.executeActionProfile(action = startingAction)
            if(results != ""):
                results = self.APManager.getActionFromName(name = nextActionName) # empty string = end

        return