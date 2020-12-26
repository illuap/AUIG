import unittest

from loguru import logger

from src.Actions.ActionProfileManager import ActionProfileManager

from src.Actions.Models.ActionProfileModel import ActionProfileModel

class ActionProfileManager_Tests(unittest.TestCase):

    testJsonPath = "data/test_actionNetwork_1.json"

    def test_getStartingAction(self):
        apa = ActionProfileManager()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getStartingAction()

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "open_missions")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getActionFromName_1(self):
        apa = ActionProfileManager()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("open_missions")

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "open_missions")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getActionFromName_2(self):
        apa = ActionProfileManager()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("dailies")

        self.assertEqual(type(results), type(ActionProfileModel()))
        self.assertEqual(results.name, "dailies")
        self.assertEqual(type(results.name), type("somestring"))
        self.assertEqual(type(results.edges), type(dict()))
        self.assertEqual(len(results.edges), 2)

    def test_getActionFromName_NoneExisting(self):
        apa = ActionProfileManager()
        apa.setJsonFile(self.testJsonPath)

        results = apa.getActionFromName("random none existing string")

        self.assertIsNone(results)

    def test_executeActionProfile_NoDelays_did_not_find(self):
        """ Ideally don't set up this case and it should move onto the next action through NO_ACTION """
        apa = ActionProfileManager()
        apa.setJsonFile(self.testJsonPath)

        action = apa.getActionFromName("dailies")

        results = apa.executeActionProfile_NoDelays(action)

        logger.debug(results)
        self.assertEqual(results.name, "open_missions")

    def test_executeActionProfile(self):
        return # TODO

