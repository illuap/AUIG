import keyboard
import time

from src.Actions.actionProfileManager import actionProfileManager
from src.Actions.ActionProfileModel import ActionProfileModel

class ActionNetwork(object):


    screenGrabber = None
    APManager = None


    def __init__(self,screenGrabber, actionProfileManager: actionProfileManager):
        self.screenGrabber = screenGrabber
        self.APManager = actionProfileManager
        # Need screen grabbber
        # Current state
        # how to execute an action
        # how to choose the first action
        # how to 

    def getStartingNode(self):
        return self.APManager.getStartingAction()

    def traverseNetwork(self, startingAction: ActionProfileModel):
        # TODO
        results = startingAction.name

        while(not keyboard.is_pressed('`') and results != ""):
            nextActionName = self.APManager.executeAction(action = startingAction)
            if(results != ""):
                results = self.APManager.getActionFromName(name = nextActionName) # empty string = end

        return