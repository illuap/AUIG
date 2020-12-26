from typing import Optional

from loguru import logger

from src.Actions.Types.ActionStatusType import ActionStatusType
from src.Actions.Models.ActionProfileModel import ActionProfileModel
from src.Clicker.Clicker import Clicker
from src.ImageRecognition.ImageRecognition import ImageRecognition


class Actions:

    @staticmethod
    def FIND_AND_CLICK(action: ActionProfileModel) -> Optional[str]:
        """ Find an image and click the image """
        ir = ImageRecognition()
        pos = ir.findSubImagePosInApplication(action.images[0])

        # Code to execute and decide what the next status should be
        if pos is not None:
            Clicker.click_at_in_app(pos)
            logger.info("Finished action " + action.name + " - " + ActionStatusType.ACTION_DONE.name)
            return Actions.__try_get_action(action, ActionStatusType.ACTION_DONE)
        else:
            logger.info("Finished action " + action.name + " - " + ActionStatusType.NO_ACTION.name)
            return Actions.__try_get_action(action, ActionStatusType.NO_ACTION)

    @staticmethod
    def __try_get_action(action: ActionProfileModel, actionStatusType: ActionStatusType) -> Optional[str]:
        if actionStatusType.name in action.edges:
            return action.edges[actionStatusType.name]
        else:
            return None

    @staticmethod
    def CHECK_AND_CLICK(action: ActionProfileModel) -> Optional[str]:
        """ Find an image and click someone else """
        ir = ImageRecognition()
        pos = ir.findSubImagePosInApplication(action.images[0])

        # Code to execute and decide what the next status should be
        if (pos != None):
            Clicker.click_at_in_app(action.coordinates[0])
            return Actions.__try_get_action(action, ActionStatusType.ACTION_DONE)
        else:
            return Actions.__try_get_action(action, ActionStatusType.NO_ACTION)
