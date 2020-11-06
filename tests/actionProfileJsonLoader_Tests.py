
import unittest
import jsonpickle

from src.Actions.actionProfileJSONloader import actionProfileJSONloader

from src.Actions.ActionProfileModel import ActionProfileModel


class actionProfileJsonLoader_Tests(unittest.TestCase):

    def test_constructor_loading_json(self):
        #Arrange/Act
        APJsonLoader = actionProfileJSONloader("./data/unitTestAP.json")

        #Assert
        self.assertEqual(APJsonLoader.actionProfileFileName, "./data/unitTestAP.json")
        self.assertGreater(len(APJsonLoader.actionProfilesDic.keys()),0)

    def test_loading_to_py_obj(self):
        # Arrange
        APJsonLoader = actionProfileJSONloader("./data/unitTestAP.json")

        # Act
        APJsonLoader.loadActionProfileToDic()

        # Assert
        self.assertEqual(list(APJsonLoader.actionProfilesDic.keys())[0], "open_missions")
        self.assertEqual(len(APJsonLoader.actionProfilesDic), 2)

    def test_add_AP_to_JSON(self):
        
        fileName = "./data/unitTestAP_add.json"
        name = "test_add_AP_to_JSON"

        # Arrange'
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = actionProfileJSONloader(fileName)

        ap = ActionProfileModel(name,
                                "findnclic",
                                {"dog":"edge1"},
                                ["sdfg/sdfgsdfg/dfg.png"],
                                [(10,200),(300,400)], 
                                10, 
                                20)
        
        # Act
        APJsonLoader.addActionProfile(ap)
    
        # Assert
        self.assertIn(name,APJsonLoader.actionProfilesDic.keys())


    def test_delete_AP_to_JSON(self):
        
        fileName = "./data/unitTestAP_delete.json"
        name = "open_missions" # AP to be deleted

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = actionProfileJSONloader(fileName)

        # Act
        APJsonLoader.deleteActionProfile(name)
    
        # Assert
        self.assertNotIn(name,APJsonLoader.actionProfilesDic.keys())

    def __setup_clean_test_JSON(self,fileName):
        base_json_file = ""
        with open("./data/unitTestAP.json", 'r') as f:
            base_json_file = jsonpickle.decode(f.read())
        with open(fileName, 'w') as f:
            f.write(jsonpickle.encode(base_json_file, unpicklable=False))


if __name__ == '__main__':
    unittest.main()
