
import unittest
import jsonpickle
import os

from src.Actions.ActionProfileAccess import ActionProfileAccess

from src.Actions.ActionProfileModel import ActionProfileModel

class ActionProfileAccess_Tests(unittest.TestCase):

    testJsonPath = "data/test_actionNetwork_1.json"

    def test_getStartingAction(self):
        apa = ActionProfileAccess()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getStartingAction()

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "open_missions")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getStartingActionName(self):
        apa = ActionProfileAccess()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getStartingActionName()

        self.assertEqual(type(results), type("string"))
        self.assertEqual(results, "open_missions")

    def test_getActionFromName_1(self):
        apa = ActionProfileAccess()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("open_missions")

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "open_missions")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getActionFromName_2(self):
        apa = ActionProfileAccess()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("dailies")

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "dailies")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getActionFromName_NoneExisting(self):
        apa = ActionProfileAccess()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("random none existing string")

        self.assertIsNone(results)
