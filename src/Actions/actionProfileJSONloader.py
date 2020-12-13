import json

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
        print("Opening: ")
        print(self.actionProfilesDic)

    def writeActionProfileDic(self):
        with open(self.actionProfileFileName, 'w') as f:
            f.write(jsonpickle.encode(self.actionProfilesDic, unpicklable=False))


    def addActionProfile(self, APModel):
        self.actionProfilesDic[APModel.name] = APModel
        self.writeActionProfileDic()

    def deleteActionProfile(self, APName):
        self.actionProfilesDic.pop(APName, None)
        self.writeActionProfileDic()

    def editActionProfile(self, APModel):
        if(APModel['name'] not in self.actionProfilesDic.keys()):
            raise Exception("Don't modify an Action Profile's name.")
        self.actionProfilesDic[APModel["name"]] = APModel
        self.writeActionProfileDic()