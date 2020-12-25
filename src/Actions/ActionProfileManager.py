import eel
import jsonpickle
import keyboard
import time

from loguru import logger

from src.Actions.ActionProfileModel import ActionProfileModel
from src.Actions.ActionProfileAccess import ActionProfileAccess
from src.Actions.Actions import Actions


class ActionProfileManager():
    actionProfileAccess = None

    def __init__(self):
        self.actionProfileAccess = ActionProfileAccess()

    def setJsonFile(self, filePath):
        self.actionProfileAccess.set_json_file(filePath)

    def getStartingAction(self) -> ActionProfileModel:
        return self.actionProfileAccess.get_starting_action()

    def getActionFromName(self, actionName) -> ActionProfileModel:
        return self.actionProfileAccess.get_action_from_name(actionName)

    # TODO: kind of odd using the above functions and these ones from the same class........
    def executeActionProfile(self, action: ActionProfileModel):
        """Takes an action profile model and decides how to perform given action
        
        :return: return the name of the next node that should be executed
        """
        # PRE-DELAY
        for i in range(0, int(action.pre_delay) * 10):
            if keyboard.is_pressed('`'):
                return ""
            eel.sleep(0.1)

        logger.debug("finished pre-delay")
        results = self.executeActionProfile_NoDelays(action)

        # POST-DELAY
        for i in range(0, int(action.post_delay) * 10):
            if keyboard.is_pressed('`'):
                return ""
            eel.sleep(0.1)

        logger.debug("finished post-delay")
        return results

    def executeActionProfile_NoDelays(self, action: ActionProfileModel):

        nextAction = ""
        if (action.actionType == "FIND_AND_CLICK"):
            nextAction = Actions.FIND_AND_CLICK(action)
        elif (action._actionType == "CHECK_AND_CLICK"):
            nextAction = Actions.CHECK_AND_CLICK(action)

        return nextAction
