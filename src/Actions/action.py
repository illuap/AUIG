
import json

class actionProfileJSONloader():
    """ Takes the actionProfiles in Json and load it into python objects
    
    TODO some decription here....
    """

    actionProfileFileName = "./data/actionProfiles.json"
    actionProfilesJSON = None

    actionProfilesDic = dict()

    def __init__(self):

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



class action():
    _name = ""
    _actionType = None
    _edges = dict()
    _coordinates = [] #(x,y)
    _images = [] # stored as 
    def __init__(self, name, actionType, edges, coordinates, images):
        self._name = name
        self._actionType = actionType
        self._edges = edges
        self._coordinates = coordinates
        self._images = images


    def execute(self):
        """ Depending on the action run a specific function. """

        if(self._actionType == "FIND_AND_CLICK"):
            self.action_FIND_AND_CLICK()
        elif(self._actionType == "CHECK_AND_CLICK"):
            self.action_CHECK_AND_CLICK()
            
    
    def action_FIND_AND_CLICK(self):
        """ Find an image and click the image """
        return 

    def action_CHECK_AND_CLICK(self):
        """ Find an image and click someone else """
        return


class actionProfile():
    """ActionProfile is an action with other meta data such as delays.

    Attributes:
        action (Action): An action that includes it's data to execute something
        preDelay (int): Delay before action (ms)
        postDelay (int): Delay after action (ms)
    
    """
    name = ""
    action = None
    preDelay = 0
    postDelay = 0

    def __init__(self, name, action, preDelay, postDelay):
        self.name = name
        self.action = action
        self.preDelay = preDelay
        self.postDelay = postDelay

    def execute(self):
        #preDelay

        # run action

        # post delay

        # go to new action????
        return


dog = actionProfileJSONloader()
dog.loadActionProfileToDic()