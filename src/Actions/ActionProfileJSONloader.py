import json

import jsonpickle

from src.Actions.ActionProfileModel import ActionProfileModel


class ActionProfileJSONloader(object):
    """ Takes the actionProfiles in Json and load it into python objects
    
    TODO some decription here....
    """

    actionProfileFileName = ""

    actionProfilesDic = dict()

    def __init__(self, actionProfileFileName="./data/actionProfiles.json"):
        self.actionProfileFileName = actionProfileFileName
        # Load json
        self.loadActionProfileToDic()

    def loadActionProfileToDic(self):
        """ Givent the json list of actionProfiles load the profile + the action """
        with open(self.actionProfileFileName, 'r') as f:
            self.actionProfilesDic = jsonpickle.decode(f.read())
        print("Opening: ")
        print(self.actionProfilesDic)

    def writeActionProfileDic(self):
        with open(self.actionProfileFileName, 'w') as f:
            jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
            f.write(jsonpickle.encode(self.actionProfilesDic, unpicklable=False))

    def get_action(self, name: str) -> ActionProfileModel:
        action = self.actionProfilesDic[name]
        return ActionProfileModel.from_dict(action)

    def add_action(self, APModel: ActionProfileModel):
        self.actionProfilesDic[APModel.name] = APModel
        self.writeActionProfileDic()

    def delete_action(self, APName: ActionProfileModel):
        self.actionProfilesDic.pop(APName, None)
        self.writeActionProfileDic()

    def edit_action(self, APModel: ActionProfileModel):
        if APModel['name'] not in self.actionProfilesDic.keys():
            raise Exception("Don't modify an Action Profile's name.")
        self.actionProfilesDic[APModel["name"]] = APModel
        self.writeActionProfileDic()
