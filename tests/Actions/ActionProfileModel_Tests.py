import unittest
import jsonpickle
import json
import os

from src.Actions.ActionProfileJSONloader import ActionProfileJSONloader

from src.Actions.ActionProfileModel import ActionProfileModel


class ActionProfileModel_Tests(unittest.TestCase):

    def test_jsonToObject_success(self):
        # arrange
        json_action = '{"name":"dsf","actionType":"FIND_AND_CLICK","edges":{"ACTION_DONE":"sdf"},"images":[' \
                      '"C:/Users/paul/Pictures/2018 Porsche 911 GT3_ You Magnificent Beast, ' \
                      'You - 1_30_files/306194_2018_Porsche_911.jpg"],"coordinates":["23","23"],"pre_delay":1,' \
                      '"post_delay":2} '
        action: ActionProfileModel = ActionProfileModel.from_json(json_action)

        self.assertEqual(action.name, "dsf")
        self.assertEqual(action.pre_delay, 1)

    def test_jsonToObject_fail(self):
        json_action = '{"name":"dsf","actionType":"FIND_AND_CLICK","edges":{"ACTION_DONE":"sdf"}} '

        try:
            action: ActionProfileModel = ActionProfileModel.from_json(json_action)
        except:
            print('success')