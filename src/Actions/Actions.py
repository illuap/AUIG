from .Types import ActionStatusType,  ActionType
from src.Actions.ActionProfileModel import ActionProfileModel
from src.Clicker import Clicker
from src.ImageRecognition import ImageRecognition

class Actions():

    @staticmethod
    def FIND_AND_CLICK(action: ActionProfileModel):
        """ Find an image and click the image """
        ir = ImageRecognition()
        pos = ir.findSubImagePosInApllication(action.images[0])

        # Code to execute and decide what the next status should be
        if(pos != None):
            Clicker.click_at_in_app(pos)
            return action.edges[ActionStatusType.ACTION_DONE.name]
        else:
            return action.edges[ActionStatusType.NO_ACTION.name]


    @staticmethod
    def CHECK_AND_CLICK(action: ActionProfileModel):
        """ Find an image and click someone else """
        ir = ImageRecognition()
        pos = ir.findSubImagePosInApllication(action.images[0])

        # Code to execute and decide what the next status should be
        if(pos != None):
            Clicker.click_at_in_app(action.coordinates[0])
            return action.edges[ActionStatusType.ACTION_DONE.name]
        else:
            return action.edges[ActionStatusType.NO_ACTION.name]