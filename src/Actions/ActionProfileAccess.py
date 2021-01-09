from typing import List

from loguru import logger

from src.Actions.Models.ActionProfileModel import ActionProfileModel
from src.Actions.ActionProfileJSONloader import ActionProfileJSONloader
from src.Actions.Models.ProfileData import ProfileData
from src.Meta.ActionProfileMetaHandler import ActionProfileMetaHandler
from src.Meta.Models.ActionProfileMetaModel import ActionProfileMetaModel


class ActionProfileAccess:
    __actionProfileJSONloader = None

    def __init__(self):
        self.__actionProfileJSONloader = ActionProfileJSONloader()

    def set_json_file(self, filePath):
        self.__actionProfileJSONloader.actionProfileFileName = filePath
        self.__actionProfileJSONloader.loadActionProfileToDic()

    # TEMP
    def get_starting_action(self) -> ActionProfileModel:
        # Default to the first one....
        profile_dir = self.__actionProfileJSONloader.actionProfileFileName
        profileData = ProfileData(profile_dir)
        results = ActionProfileMetaHandler.get_meta_data(profileData)

        # If there is no initial starting node set one, ONLY IF THERE ARE ANY NODES
        if results.starting_node_name is None or results.starting_node_name == "":
            keys = self.__actionProfileJSONloader.actionProfilesDic.keys()
            if len(keys) >= 1:
                new_starting_node = ActionProfileMetaModel(starting_node_name=list(keys)[0])

                ActionProfileMetaHandler.set_meta_data(profileData, new_starting_node)
                # This is redundant but prevents any data desync issues
                results = ActionProfileMetaHandler.get_meta_data(profileData)

        return self.__actionProfileJSONloader.get_action(results.starting_node_name)


    def get_action_from_name(self, name) -> ActionProfileModel:
        ap_dict = self.__actionProfileJSONloader.actionProfilesDic.get(name, None)
        if ap_dict:
            ap_obj = ActionProfileModel.from_dict(ap_dict)
            return ap_obj
        else:
            return None

    def add_action(self, action: ActionProfileModel):
        self.__actionProfileJSONloader.add_action(action)

    def delete_action(self, name: str):
        self.__actionProfileJSONloader.delete_action(name)

    def edit_action(self, action: ActionProfileModel):
        self.__actionProfileJSONloader.edit_action(action)

    def get_all_edges(self) -> List[str]:
        edges = []
        for val in self.__actionProfileJSONloader.actionProfilesDic.keys():
            edges.append(val)
        return edges

    def set_starting_action(self, name: str):
        try:
            profile_data = ProfileData(self.__actionProfileJSONloader.actionProfileFileName)

            new_start = self.__actionProfileJSONloader.get_action(name)
            ActionProfileMetaHandler.set_meta_data(profile_data, new_start)
            return True
        except:
            logger.error("Failed to set the starting action.")
            return False
