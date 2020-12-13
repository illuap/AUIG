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
        self.assertTrue(ProfileViewer.CheckIfProfileExistsInRoot('./data/unitTestAP.json'))
        
    def test_CheckIfProfileExistsInDataFolder(self):
        self.assertTrue(ProfileViewer.CheckIfProfileExistsInDataFolder('./data/unitTestAP.json'))