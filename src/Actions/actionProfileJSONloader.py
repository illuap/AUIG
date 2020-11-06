import json

from .action import action, actionProfile

class actionProfileJSONloader(object):
    """ Takes the actionProfiles in Json and load it into python objects
    
    TODO some decription here....
    """

    actionProfileFileName = ""
    actionProfilesJSON = None

    actionProfilesDic = dict()

    def __init__(self, actionProfileFileName = "./data/actionProfiles.json"):
        self.actionProfileFileName = actionProfileFileName
        # Load json
        with open(self.actionProfileFileName, 'r') as f:
            self.actionProfilesJSON = json.load(f)

    def __loadAction(self,profileName):
        """ Given the json of a specific action load it (private)"""
        return action(name = profileName, 
                        actionType = self.actionProfilesJSON[profileName]['actionType'],
                        edges = self.actionProfilesJSON[profileName]['edges'],
                        coordinates = None,
                        images = None)

    def __loadActionProfile(self,profileName,action):
        return actionProfile(name = profileName, 
                                action = action, 
                                preDelay = 0, 
                                postDelay = 0)


    def loadActionProfileToDic(self):
        """ Givent the json list of actionProfiles load the profile + the action """
        for profile in self.actionProfilesJSON:
            action = self.__loadAction(profile)
            actionProfile = self.__loadActionProfile(profile,action)

            self.actionProfilesDic[profile] = actionProfile
        #Grab into

        #load the action

