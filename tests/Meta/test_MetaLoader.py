import os
import unittest

from src.Meta.MetaLoader import MetaLoader


class ProfileViewer_Tests(unittest.TestCase):
    expected = "./data/unitTestAP_meta.json"

    def test_get_file_path(self):
        dir = "./data/unitTestAP.json"

        loader = MetaLoader(dir)
        self.assertEqual(self.expected, loader.get_file_path())

    def test_save_metadata(self):
        dir = "./data/unitTestAP.json"

        loader = MetaLoader(dir)
        loader.save_metadata()
        self.assertEqual(self.expected, loader.get_file_path())
        self.assertTrue(os.path.exists(self.expected))

    def test_save_metadata_item_check(self):
        dir = "./data/empty.json"
        expected_dir = "./data/empty_meta.json"

        loader = MetaLoader(dir)
        loader.set_data({"key1": "value1"})
        results = loader.get_data()
        loader.save_metadata()

        self.assertEqual(expected_dir, loader.get_file_path())
        self.assertTrue(os.path.exists(expected_dir))
        self.assertIn("key1", results.keys())
        self.assertEqual(results["key1"], "value1")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.expected)
        return
