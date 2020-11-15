import jsonpickle
import json

from json import JSONEncoder

class ActionProfileModel():
    name = ""
    actionType = ""
    edges = dict()
    images = []
    coordinates = []
    pre_delay = 0
    post_delay = 0

    def __init__(self, name = None, actionType = None, edges = None, images = None, coordinates = None, pre_delay = None, post_delay = None):
        self.name = name
        self.actionType = actionType
        self.edges = edges
        self.images = images
        self.coordinates = coordinates
        self.pre_delay = pre_delay
        self.post_delay = post_delay
        
    def toJSON(self):
        return jsonpickle.encode(self, unpicklable=False)
        #return json.dumps(self, default=lambda o: o.__dict__, indent=4)
        
    @staticmethod
    def dict2obj(dict1): 
        # using json.loads method and passing json.dumps 
        # method and custom object hook as arguments 
        print(dict1, type(dict1))
        return json.loads(json.dumps(dict1), object_hook=ActionProfileModel) 
    @staticmethod
    def json2obj(someJson): 
        # using json.loads method and passing json.dumps 
        # method and custom object hook as arguments 
        return json.loads(someJson, object_hook=ActionProfileModel) 

class ActionProfileModel_Encoder(JSONEncoder):
        def default(self, o): return o.__dict__

def studentDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Student':
        return Student(obj['rollNumber'], obj['name'], obj['marks'])
    return obj
