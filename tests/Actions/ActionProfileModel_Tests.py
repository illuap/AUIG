
import unittest
import jsonpickle
import json
import os

from src.Actions.actionProfileJSONloader import actionProfileJSONloader

from src.Actions.ActionProfileModel import ActionProfileModel

class ActionProfileModel_Tests(unittest.TestCase):

    def dog(self):
        return
    # def test_convert_json_to_obj(self):
    #     someJson = json.dumps({"open_missions": {
    #                 "name": "open_missions",
    #                 "actionType": "FIND_AND_CLICK",
    #                 "edges": { "ACTION_DONE": "dailies",
    #                             "NO_ACTION" : "dailies" },
    #                 "images": ["images/test/actionNetwork_test_1.png"],
    #                 "coordinates": [
    #                 ],
    #                 "pre_delay": 10,
    #                 "post_delay": 20
    #             }})

    #     results = ActionProfileModel.json2obj(someJson)

    #     print(results, type(results))
    #     dog = results.name
    #     print(dog, type(dog))
    #     self.assertEqual(results.name, "open_missions")