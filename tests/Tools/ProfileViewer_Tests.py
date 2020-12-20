import unittest
import cv2

from src.Tools.ProfileViewer import ProfileViewer

class ProfileViewer_Tests(unittest.TestCase):


    def test_GetListOfProfiles(self):
        profiles = ProfileViewer.GetAllProfiles()

        sampleFile = "unitTestAP.json"

        print(profiles)

        self.assertTrue(sampleFile in profiles)

    
    def test_CheckIfProfileExistsInRoot(self):
        self.assertFalse(ProfileViewer.CheckIfProfileExistsInRoot('unitTestAP.json'))
        
    def test_CheckIfProfileExistsInDataFolder(self):
        self.assertFalse(ProfileViewer.CheckIfProfileExistsInDataFolder('DOESNOTEXITFILE.json'))
        self.assertTrue(ProfileViewer.CheckIfProfileExistsInDataFolder('unitTestAP.json'))

    def test_GetFileDirForDataFile(self):
        results = ProfileViewer.GetFileDirForDataFile("unitTestAP.json")
        self.assertEqual("./data/unitTestAP.json", results)