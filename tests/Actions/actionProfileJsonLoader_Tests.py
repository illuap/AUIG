
import unittest
import jsonpickle
import os

from src.Actions.actionProfileJSONloader import actionProfileJSONloader

from src.Actions.ActionProfileModel import ActionProfileModel

FILEPATH_ORIGINAL_JSON = "./data/unitTestAP.json"
class actionProfileJsonLoader_Tests(unittest.TestCase):

    def test_constructor_loading_json(self):
        #Arrange/Act
        APJsonLoader = actionProfileJSONloader(FILEPATH_ORIGINAL_JSON)

        #Assert
        self.assertEqual(APJsonLoader.actionProfileFileName, FILEPATH_ORIGINAL_JSON)
        self.assertGreater(len(APJsonLoader.actionProfilesDic.keys()),0)

    def test_loading_to_py_obj(self):
        # Arrange
        APJsonLoader = actionProfileJSONloader(FILEPATH_ORIGINAL_JSON)

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

    def test_edit_AP_to_JSON(self):
        
        fileName = "./data/unitTestAP_edit.json"
        value = 55 # modified AP name

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = actionProfileJSONloader(fileName)

        # Act
        modifiedAP = APJsonLoader.actionProfilesDic[next(iter(APJsonLoader.actionProfilesDic))]
        og_name = modifiedAP["name"]
        og_value = modifiedAP["pre_delay"]
        modifiedAP["pre_delay"] = value
        APJsonLoader.editActionProfile(modifiedAP)
    
        # Assert
        self.assertEqual(value,APJsonLoader.actionProfilesDic[og_name]["pre_delay"])

    def test_edit_NAME_AP_to_JSON(self):
        
        fileName = "./data/unitTestAP_edit.json"
        name = "flipping" # modified AP name

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = actionProfileJSONloader(fileName)
        
        # Act
        with self.assertRaises(Exception) as context:
            modifiedAP = APJsonLoader.actionProfilesDic[next(iter(APJsonLoader.actionProfilesDic))]
            modifiedAP["name"] = name
            APJsonLoader.editActionProfile(modifiedAP)
    
        # Assert
        self.assertTrue(context.exception)

    @classmethod
    def tearDownClass(cls):
        filesToRemove = ["./data/unitTestAP_edit.json",
                            "./data/unitTestAP_delete.json",
                            "./data/unitTestAP_add.json"]

        for file in filesToRemove:
            os.remove(file)


    # OLD FUCTION
    def __setup_clean_test_JSON(self,fileName):
        base_json_file = ""
        with open(FILEPATH_ORIGINAL_JSON, 'r') as f:
            base_json_file = jsonpickle.decode(f.read())
        with open(fileName, 'w+') as f:
            f.write(jsonpickle.encode(base_json_file, unpicklable=False))


if __name__ == '__main__':
    unittest.main()