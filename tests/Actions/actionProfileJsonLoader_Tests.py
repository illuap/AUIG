import unittest
import jsonpickle
import os

from src.Actions.ActionProfileJSONloader import ActionProfileJSONloader

from src.Actions.Models.ActionProfileModel import ActionProfileModel

FILEPATH_ORIGINAL_JSON = "./data/test_actionNetwork_2.json"


class actionProfileJsonLoader_Tests(unittest.TestCase):

    def test_constructor_loading_json(self):
        # Arrange/Act
        APJsonLoader = ActionProfileJSONloader(FILEPATH_ORIGINAL_JSON)

        # Assert
        self.assertEqual(APJsonLoader.actionProfileFileName, FILEPATH_ORIGINAL_JSON)
        self.assertGreater(len(APJsonLoader.actionProfilesDic.keys()), 0)

    def test_loading_to_py_obj(self):
        # Arrange
        APJsonLoader = ActionProfileJSONloader(FILEPATH_ORIGINAL_JSON)

        # Act
        APJsonLoader.loadActionProfileToDic()

        # Assert
        self.assertEqual(list(APJsonLoader.actionProfilesDic.keys())[0], "open_missions")
        self.assertEqual(len(APJsonLoader.actionProfilesDic), 2)

    def test_get_action(self):
        fileName = "./data/unitTestAP_get.json"

        name = "test_get_action"

        # Arrange'
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        ap = ActionProfileModel(name,
                                "findnclic",
                                {"dog": "edge1"},
                                ["sdfg/sdfgsdfg/dfg.png"],
                                [(10, 200), (300, 400)],
                                10,
                                20)
        action = APJsonLoader.add_action(ap)

        # Act
        action = APJsonLoader.get_action(name)

        # Assert
        self.assertEqual(action.name, name)
        self.assertEqual(action.actionType, "findnclic")

    def test_self_validate_file(self):
        fileName = "./data/unitTestAP_self_validate.json"
        name = "test1"

        # Arrange'
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        ap = ActionProfileModel(name,
                                "findnclic",
                                {"dog": "edge1"},
                                ["sdfg/sdfgsdfg/dfg.png"],
                                [(10, 200), (300, 400)],
                                10,
                                20)

        # Act
        APJsonLoader.add_action(ap)

        APJsonLoader2 = ActionProfileJSONloader(fileName)
        results = APJsonLoader2.get_action(ap.name)
        # Assert
        self.assertIn(name, results.name)

    def test_add_AP_to_JSON(self):
        fileName = "./data/unitTestAP_add.json"
        name = "test_add_AP_to_JSON"

        # Arrange'
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        ap = ActionProfileModel(name,
                                "findnclic",
                                {"dog": "edge1"},
                                ["sdfg/sdfgsdfg/dfg.png"],
                                [(10, 200), (300, 400)],
                                10,
                                20)

        # Act
        APJsonLoader.add_action(ap)

        # Assert
        self.assertIn(name, APJsonLoader.actionProfilesDic.keys())
        self.assertIn(name, APJsonLoader.actionProfilesDic.keys())

    def test_delete_AP_to_JSON(self):
        fileName = "./data/unitTestAP_delete.json"
        name = "open_missions"  # AP to be deleted

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        # Act
        APJsonLoader.delete_action(name)

        # Assert
        self.assertNotIn(name, APJsonLoader.actionProfilesDic.keys())

    def test_edit_AP_to_JSON(self):
        fileName = "./data/unitTestAP_edit.json"
        value = 55  # modified AP name

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        # Act
        modifiedAP = APJsonLoader.actionProfilesDic[next(iter(APJsonLoader.actionProfilesDic))]
        og_name = modifiedAP["name"]
        og_value = modifiedAP["pre_delay"]
        modifiedAP["pre_delay"] = value
        APJsonLoader.edit_action(modifiedAP)

        # Assert
        self.assertEqual(value, APJsonLoader.actionProfilesDic[og_name]["pre_delay"])

    def test_edit_NAME_AP_to_JSON(self):
        fileName = "./data/unitTestAP_edit.json"
        name = "flipping"  # modified AP name

        # Arrange
        self.__setup_clean_test_JSON(fileName)
        APJsonLoader = ActionProfileJSONloader(fileName)

        # Act
        with self.assertRaises(Exception) as context:
            modifiedAP = APJsonLoader.actionProfilesDic[next(iter(APJsonLoader.actionProfilesDic))]
            modifiedAP["name"] = name
            APJsonLoader.edit_action(modifiedAP)

        # Assert
        self.assertTrue(context.exception)

    @classmethod
    def tearDownClass(cls):
        filesToRemove = ["./data/unitTestAP_edit.json",
                         "./data/unitTestAP_delete.json",
                         "./data/unitTestAP_add.json"]

        for file in filesToRemove:
            os.remove(file)

    def __setup_clean_test_JSON(self, fileName):
        base_json_file = ""
        with open(FILEPATH_ORIGINAL_JSON, 'r') as f:
            base_json_file = jsonpickle.decode(f.read())
        with open(fileName, 'w+') as f:
            f.write(jsonpickle.encode(base_json_file, unpicklable=False))


if __name__ == '__main__':
    unittest.main()
