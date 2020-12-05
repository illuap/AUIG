from enums.actionTypes import actionTypes
import json

actionProfileFileName = 'actionProfiles.json'
# make singleton?
if 'ActionProfiles' not in vars():
    with open(actionProfileFileName, 'r') as f:
        ActionProfiles = json.load(f)

DELAY_KEY = "delays"


# an individual action profile
class ActionProfileV2:
    uniqueName = None
    action = None
    delays = None

    # new profile
    def __init__(self, uniquename, action=None, delays=None):
        # TODO implement this
        return

    def SetAction(self, new_action):
        # TODO implement this
        return

    def RunAction(self):
        # TODO pre pre delay
        self.action.run()
        # TODO insert post delay
        return
