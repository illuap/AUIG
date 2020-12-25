import keyboard
import time
import json

from loguru import logger

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

    def traverseNetwork(self, starting_action: ActionProfileModel = None):
        logger.info("Starting Network Traverse!")

        if not starting_action:
            logger.info("Getting starting action!")
            starting_action = self.APManager.getStartingAction()
        # TODO
        results = starting_action
        while not keyboard.is_pressed('`') and results != "":

            logger.info("Starting action: " + results.name)
            next_action_name = self.APManager.executeActionProfile(action=results)
            if results != "":
                results = self.APManager.getActionFromName(actionName=next_action_name)  # empty string = end
            logger.info("Queuing up next action: " + results.name)

        logger.info("Ending network Traverse!")

        return

    def getActionsInNetwork(self):
        return json.dumps(self.APManager.actionProfileAccess.__actionProfileJSONloader.actionProfilesDic, indent=4)
        # self.APManager
