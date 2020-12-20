import jsonpickle
import json
from typing import List, Dict
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from json import JSONEncoder

from marshmallow.fields import String


@dataclass_json
@dataclass
class ActionProfileModel:
    name: str
    actionType: str
    edges: Dict[str, str]
    images: List[str]
    coordinates: List[List[int]]
    pre_delay: int
    post_delay: int

    def __init__(self, name=None, actionType=None, edges=None, images=None, coordinates=None, pre_delay=None,
                 post_delay=None):
        self.name = name
        self.actionType = actionType
        self.edges = edges
        self.images = images
        self.coordinates = coordinates
        self.pre_delay = pre_delay
        self.post_delay = post_delay
