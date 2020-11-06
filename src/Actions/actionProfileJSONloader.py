import json

from .action import action, actionProfile
import jsonpickle



class actionProfileJSONloader(object):
    """ Takes the actionProfiles in Json and load it into python objects
    
    TODO some decription here....
    """

    actionProfileFileName = ""

    actionProfilesDic = dict()

    def __init__(self, actionProfileFileName = "./data/actionProfiles.json"):
        self.actionProfileFileName = actionProfileFileName
        # Load json
        self.loadActionProfileToDic()


    def loadActionProfileToDic(self):
        """ Givent the json list of actionProfiles load the profile + the action """
        with open(self.actionProfileFileName, 'r') as f:
            self.actionProfilesDic = jsonpickle.decode(f.read())

    def writeActionProfileDic(self):
        with open(self.actionProfileFileName, 'w') as f:
            f.write(jsonpickle.encode(self.actionProfilesDic, unpicklable=False))


    def addActionProfile(self, APModel):
        self.actionProfilesDic[APModel.name] = APModel
        self.writeActionProfileDic()

    def deleteActionProfile(self, APName):
        self.actionProfilesDic.pop(APName, None)
        self.writeActionProfileDic()

    #TODO test
    def editActionProfile(self, APModel):
        self.actionProfilesDic[actionProfile.name] = APModel
        self.writeActionProfileDic()