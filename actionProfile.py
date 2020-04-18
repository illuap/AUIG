

from enums.actionTypes import actionTypes
import json


if('ActionProfiles' not in vars()): 
    with open('actionProfiles.json', 'r') as f:
        ActionProfiles = json.load(f)


# an individual action profile
class actionProfile:
    uniqueName = None
    actionType = None
    data = None

    # new profile
    def __init__(self, uniqueName, actionType = None, data = None):
        if(actionType == None):
            self.uniqueName = uniqueName
            print("==LOADING " + uniqueName + "===")
            print(ActionProfiles[uniqueName])

            self.actionType = actionTypes[ActionProfiles[uniqueName]["actionType"]]
            self.data = ActionProfiles[uniqueName]["data"]

            print("===Data===")
            print(self.data)

            print(self.actionType)
        else:
            self.uniqueName = uniqueName
            self.actionType = actionType
            self.data = data

    #def save(self):