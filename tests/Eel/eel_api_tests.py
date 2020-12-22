import os
import unittest
import cv2
import json

import jsonpickle

from src.ImageGrabber.ImageGrabber import ImageGrabber
from src.WebApp.AUIRG_WebApp import AUIRG_WebApp
from src.WebApp.EelAPI import *

FILEPATH_ORIGINAL_JSON = "./data/unitTestAP.json"


class Eel_API_Tests(unittest.TestCase):

    def test_addActionToProfilePY(self):
        app: AUIRG_WebApp = AUIRG_WebApp.get_instance()

        tempFileName = "./data/unitTestAP_ADD_EEL.json"
        self.__setup_clean_test_JSON(tempFileName)

        name = "TESTING_ADD"
        ap = ActionProfileModel(name,
                                "findnclic",
                                {"dog": "edge1"},
                                ["sdfg/sdfgsdfg/dfg.png"],
                                [(10, 200), (300, 400)],
                                10,
                                20)

        print(ap)
        json_raw = jsonpickle.encode(ap,unpicklable=False)

        set_profile(tempFileName)
        statusCode = addActionToProfilePY(json_raw)

        self.assertEqual(statusCode.Code, ResultCode.SUCCESS)


        f = open("./data/test_actionNetwork_1.json", "r")
        json_raw = f.read()
        f.close()
        print("Printing JSON: ")
        print(json_raw)

        results = app.apManager.getActionFromName(name)
        self.assertIsNotNone(results)
        self.assertEqual(results.name, name)


    @classmethod
    def tearDownClass(cls):
        filesToRemove = ["./data/unitTestAP_ADD_EEL.json"]

        for file in filesToRemove:
            os.remove(file)

    def __setup_clean_test_JSON(self, fileName):
        base_json_file = ""
        with open(FILEPATH_ORIGINAL_JSON, 'r') as f:
            base_json_file = jsonpickle.decode(f.read())
        with open(fileName, 'w+') as f:
            f.write(jsonpickle.encode(base_json_file, unpicklable=False))
