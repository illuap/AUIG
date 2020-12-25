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

        next_action: ActionProfileModel = starting_action
        while not keyboard.is_pressed('`') and next_action is not None: #TODO get rid of the multiple keyboard press checks

            logger.info("Starting action: " + next_action.name)
            next_action = self.APManager.executeActionProfile(action=next_action)
            if next_action is None:
                logger.info("Ending Traversal Early!")
                break

            logger.info("Queuing up next action: " + next_action.name)

        logger.info("Ended network Traverse!")

        return

    def getActionsInNetwork(self):
        return json.dumps(self.APManager.actionProfileAccess.__actionProfileJSONloader.actionProfilesDic, indent=4)
        # self.APManager
