from typing import Optional

import eel
import keyboard

from loguru import logger

from src.Actions.Models.ActionProfileModel import ActionProfileModel
from src.Actions.ActionProfileAccess import ActionProfileAccess
from src.Actions.Actions import Actions


class ActionProfileManager:
    actionProfileAccess = None

    def __init__(self):
        self.actionProfileAccess = ActionProfileAccess()

    def setJsonFile(self, filePath):
        self.actionProfileAccess.set_json_file(filePath)

    def getStartingAction(self) -> ActionProfileModel:
        results = self.actionProfileAccess.get_starting_action()
        return results

    def setStartingActionByName(self, name) -> bool:
        if name not in self.actionProfileAccess.get_all_edges():
            raise Exception("Starting Action not found")
        return self.actionProfileAccess.set_starting_action(name)

    def getActionFromName(self, actionName) -> ActionProfileModel:
        return self.actionProfileAccess.get_action_from_name(actionName)

    # TODO: kind of odd using the above functions and these ones from the same class........ (MIGHT WANA BREAK APART)
    def executeActionProfile(self, action: ActionProfileModel) -> Optional[ActionProfileModel]:
        """Takes an action profile model and decides how to perform given action
        
        :return: return the next node that should be executed
        """
        # PRE-DELAY
        for i in range(0, int(action.pre_delay)):
            if keyboard.is_pressed('`'):
                logger.info("Keyboard Exit")
                return None
            eel.sleep(0.001)

        logger.debug("finished pre-delay")
        results = self.executeActionProfile_NoDelays(action)

        # POST-DELAY
        for i in range(0, int(action.post_delay)):
            if keyboard.is_pressed('`'):
                logger.info("Keyboard Exit")
                return None
            eel.sleep(0.001)

        logger.debug("finished post-delay")
        return results


    # TODO MIGHT WANA BREAK APART
    def executeActionProfile_NoDelays(self, action: ActionProfileModel) -> Optional[ActionProfileModel]:
        logger.info("Executing " + action.name + " - " + action.actionType)
        next_action_name = None
        if action.actionType == "FIND_AND_CLICK":
            next_action_name = Actions.FIND_AND_CLICK(action)
        elif action.actionType == "CHECK_AND_CLICK":
            next_action_name = Actions.CHECK_AND_CLICK(action)

        if next_action_name is None:
            return None

        return self.getActionFromName(next_action_name)
