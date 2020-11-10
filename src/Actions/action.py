
import json

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


# dog = actionProfileJSONloader()
# dog.loadActionProfileToDic()










