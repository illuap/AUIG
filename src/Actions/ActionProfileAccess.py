import jsonpickle
import json
import keyboard
import time

from src.Actions.ActionProfileModel import ActionProfileModel
from src.Actions.ActionProfileJSONloader import ActionProfileJSONloader
from src.Actions.Actions import Actions


class ActionProfileAccess:
    __actionProfileJSONloader = None

    def __init__(self):
        self.__actionProfileJSONloader = ActionProfileJSONloader()

    def set_json_file(self, filePath):
        self.__actionProfileJSONloader.actionProfileFileName = filePath
        self.__actionProfileJSONloader.loadActionProfileToDic()

    # TEMP
    def get_starting_action(self):
        # Default to the first one....
        first_ap_dict = next(iter(self.__actionProfileJSONloader.actionProfilesDic.values()))
        first_ap_obj = ActionProfileModel.from_dict(first_ap_dict)
        return first_ap_obj

    # TEMP
    def get_starting_action_name(self) -> ActionProfileModel:
        # Default to the first one....`
        return next(iter(self.__actionProfileJSONloader.actionProfilesDic.values()))['name']

    def get_action_from_name(self, name) -> ActionProfileModel:
        ap_dict = self.__actionProfileJSONloader.actionProfilesDic.get(name, None)
        if ap_dict:
            ap_obj = ActionProfileModel.from_dict(ap_dict)
            return ap_obj
        else:
            return None

    def add_action(self, action: ActionProfileModel):
        self.__actionProfileJSONloader.add_action(action)

    def delete_action(self, name: str):
        self.__actionProfileJSONloader.delete_action(name)

    def edit_action(self, action: ActionProfileModel):
        self.__actionProfileJSONloader.edit_action(action)
