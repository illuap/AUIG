
import jsonpickle
import json
import keyboard
import time

from src.Actions.ActionProfileModel import ActionProfileModel
from src.Actions.actionProfileJSONloader import actionProfileJSONloader
from src.Actions.Actions import Actions

class ActionProfileAccess():

    actionProfileJSONloader = None
    def __init__(self):
        self.actionProfileJSONloader = actionProfileJSONloader()

    def setJsonFile(self, filePath):
        self.actionProfileJSONloader.actionProfileFileName = filePath
        self.actionProfileJSONloader.loadActionProfileToDic()

    # TEMP
    def getStartingAction(self):
        # Default to the first one....
        first_AP_dict = next(iter(self.actionProfileJSONloader.actionProfilesDic.values()))
        first_AP_obj = ActionProfileModel(**first_AP_dict)
        return first_AP_obj

    # TEMP
    def getStartingActionName(self):
        # Default to the first one....
        return next(iter(self.actionProfileJSONloader.actionProfilesDic.values()))['name']
        
    def getActionFromName(self, name):
        ap_dict = self.actionProfileJSONloader.actionProfilesDic.get(name,None)
        if ap_dict:
            ap_obj = ActionProfileModel(**ap_dict)
            return ap_obj
        else:
            return None
