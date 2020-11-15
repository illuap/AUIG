import unittest
import cv2

from src.ActionNetwork.ActionNetwork import ActionNetwork
from src.ImageGrabber.ImageGrabber import ImageGrabber
from src.Actions.ActionProfileManager import ActionProfileManager

class ActionNetwork_Tests_Manual(unittest.TestCase):

    def dog(self):
        return
    # def test_traverseNetwork(self):
    #     """ 
    #     This test is overall very complex as it is almost a while integration test.

    #     This requires some setup. 

    #     1) Open Nox to KR homescreen/town (requires us to see the portal)
    #     2) Click on portal 
    #     3) Should exit. 

    #     """
    #     apm = ActionProfileManager()
    #     print("hmm")
    #     apm.setJsonFile("data/test_actionNetwork_1.json")
    #     an = ActionNetwork(apm)

        
    #     an.traverseNetwork()
    #     return
