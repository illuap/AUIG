
import jsonpickle
import keyboard
import time

from src.Actions.ActionProfileModel import ActionProfileModel
from src.Actions.actionProfileJSONloader import actionProfileJSONloader
from src.Actions.Actions import Actions

class actionProfileManager():

    actionProfileJSONloader = None
    def __init__(self):
        self.actionProfileJSONloader = actionProfileJSONloader()
        self.actionProfileJSONloader.loadActionProfileToDic() # Refresh the dictionary just in case.

    # TEMP
    def getStartingAction(self):
        # Default to the first one....
        return jsonpickle.decode(next(iter(self.actionProfileJSONloader.actionProfilesDic)))
    # TEMP
    def getStartingActionName(self):
        # Default to the first one....
        return next(iter(self.actionProfileJSONloader.actionProfilesDic))['name']

        
    def getActionFromName(self, name):
        return jsonpickle.decode(self.actionProfileJSONloader.actionProfilesDic[name])

    def executeActionProfile(self, action: ActionProfileModel):
        """Takes an action profile model and decides how to perform given action
        
        :return: return the name of the next node that should be executed
        """
        # PRE-DELAY
        for i in range(0,int(action.pre_delay*100)):
            if(keyboard.is_pressed('`')):
                return ""
            time.sleep(0.01)

        results = self.executeActionProfile_NoDelays(action)


        # POST-DELAY
        for i in range(0,int(action.post_delay*100)):
            if(keyboard.is_pressed('`')):
                return ""
            time.sleep(0.01)

        return results


    def executeActionProfile_NoDelays(self, action: ActionProfileModel):

        nextAction = ""
        if(action.actionType == "FIND_AND_CLICK"):
            nextAction = Actions.FIND_AND_CLICK(action)
        elif(action._actionType == "CHECK_AND_CLICK"):
            nextAction = Actions.CHECK_AND_CLICK(action)

        return nextAction
    