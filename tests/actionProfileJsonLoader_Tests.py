
import unittest

from src.Actions.actionProfileJSONloader import actionProfileJSONloader


class actionProfileJsonLoader_Tests(unittest.TestCase):

    def test_constructor_loading_json(self):
        #Arrange/Act
        APJsonLoader = actionProfileJSONloader("./data/unitTestAP.json")

        #Assert
        self.assertEqual(APJsonLoader.actionProfileFileName, "./data/unitTestAP.json")
        self.assertEqual(len(APJsonLoader.actionProfilesJSON),2)

    def test_loading_to_py_obj(self):
        # Arrange
        APJsonLoader = actionProfileJSONloader("./data/unitTestAP.json")

        # Act
        APJsonLoader.loadActionProfileToDic()

        # Assert
        self.assertEqual(list(APJsonLoader.actionProfilesDic.keys())[0], "open_missions")
        self.assertEqual(len(APJsonLoader.actionProfilesDic), 2)




if __name__ == '__main__':
    unittest.main()
