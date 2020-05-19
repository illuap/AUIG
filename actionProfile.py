

from enums.actionTypes import actionTypes
import json

actionProfileFileName = 'actionProfiles.json'

if('ActionProfiles' not in vars()): 
    with open(actionProfileFileName, 'r') as f:
        ActionProfiles = json.load(f)


DELAY_KEY = "delays"

# an individual action profile
class actionProfile:
    uniqueName = None
    actionType = None
    edges = None
    data = None
    delays = None

    # new profile
    def __init__(self, uniqueName, actionType = None, edges = None, data = None, delays = None):
        # LOAD EXISTING
        #TODO do more error checking here?
        if(actionType == None):
            self.uniqueName = uniqueName
            print("==LOADING " + uniqueName + "===")
            print(ActionProfiles[uniqueName])

            self.actionType = actionTypes[ActionProfiles[uniqueName]["actionType"]]
            self.data = ActionProfiles[uniqueName]["data"]
 
            print("===Data===")
            print(self.data)

            print(self.actionType)

            print("===EDGES===")
            self.edges = ActionProfiles[uniqueName]["edges"]

            print("===DELAYS===")
            self.GetAndSetDelays()
        else:
            self.uniqueName = uniqueName
            self.actionType = actionType
            self.edges = edges
            self.data = data
            self.delays = delays

            self.SetDefaultDelaysIfEmpty()

    def save(self):
        print("Saving " + self.uniqueName)
        # BUILD JSON
        json_data = { 
            "actionType": self.actionType,
            "edges": self.edges,
            "data": self.data,
            "delays": self.delays
        }

        # GET JSON AND SAVE
        if(self.uniqueName in ActionProfiles):
            print("[ERROR] " + self.uniqueName + " ALREADY EXISTS")
            return

        ActionProfiles[self.uniqueName] = json_data

        with open(actionProfileFileName, 'w') as f:
            json.dump(ActionProfiles, f, indent=4)

    def SetDefaultDelaysIfEmpty(self):
        if(ActionProfiles == None or self.uniqueName not in ActionProfiles.keys()):
            self.delays = {}
            self.delays["START_DELAY"] = 0
            self.delays["POST_DELAY"] = 0
            return True
        if(DELAY_KEY not in ActionProfiles[self.uniqueName].keys()):
            self.delays = {}
            self.delays["START_DELAY"] = 0
            self.delays["POST_DELAY"] = 0
            return True
        else:
            return False

    def GetAndSetDelays(self):
        if(not self.SetDefaultDelaysIfEmpty()): #if it isn't empty grab from file.
            self.delays = ActionProfiles[self.uniqueName][DELAY_KEY]
            if("START_DELAY" not in self.delays.keys()):
                self.delays["START_DELAY"] = 0
            if("POST_DELAY" not in self.delays.keys()):
                self.delays["POST_DELAY"] = 0
