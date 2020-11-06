import jsonpickle

class ActionProfileModel():
    name = ""
    actionType = ""
    edges = dict()
    images = []
    coordinates = []
    pre_delay = 0
    post_delay = 0

    def __init__(self, name, actionType, edges, images, coordinates, pre_delay, post_delay):
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

