import os
import unittest

from src.Actions.Models.ProfileData import ProfileData
from src.Meta.ActionProfileMetaHandler import ActionProfileMetaHandler
from src.Meta.MetaLoader import MetaLoader
from src.Meta.Models.ActionProfileMetaModel import ActionProfileMetaModel
from tests.Meta.stub_meta import stub_meta
from tests.UnitTestHelpers.FileGenerator import FileGenerator


class test_ActionProfileMetaHandler(unittest.TestCase):
    __files_to_be_removed = []
    def test_getset_meta_data(self):
        sampleFile = FileGenerator.GenerateCopyOfFile(stub_meta.emptyFileDir)
        self.__files_to_be_removed.append(sampleFile)

        data = ProfileData(sampleFile)
        ActionProfileMetaHandler.set_meta_data(data, stub_meta.sampleMetaData)

        results = ActionProfileMetaHandler.get_meta_data(data)

        print(results.starting_node_name)
        print(type(results))

        self.assertIsInstance(results, ActionProfileMetaModel)
        self.assertEqual(stub_meta.sampleMetaData.starting_node_name, results.starting_node_name)



    @classmethod
    def tearDownClass(cls):
        for file in cls.__files_to_be_removed:
            os.remove(file)
            os.remove(MetaLoader(file).get_file_path())

