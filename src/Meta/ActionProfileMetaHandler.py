from typing import Dict

from src.Actions.Models.ProfileData import ProfileData
from src.Meta.MetaLoader import MetaLoader
from src.Meta.Models.ActionProfileMetaModel import ActionProfileMetaModel


class ActionProfileMetaHandler:


    @staticmethod
    def get_meta_data(profileData: ProfileData) -> ActionProfileMetaModel:
        loader = MetaLoader(profileData.file_path)
        data = loader.get_data()

        if not ActionProfileMetaHandler.can_deserialize(data):
            data = ActionProfileMetaHandler.create_default_data(data)
            loader.set_data(data)
            data = loader.get_data()
        return ActionProfileMetaModel.from_dict(data)

    @staticmethod
    def set_meta_data(profileData: ProfileData, data: ActionProfileMetaModel):
        loader = MetaLoader(profileData.file_path)
        loader.set_data(data)

    @staticmethod
    def can_deserialize(data:Dict):
        can = True
        if "starting_node_name" not in data.keys():
            can = False
        return can


    @staticmethod
    def create_default_data(data: Dict):
        # make sure to carry over any variables when creating a new one
        # This is to make sure that it doesn't override any partially finished data
        obj = ActionProfileMetaModel("")
        if "starting_node_name" in data.keys():
            obj.starting_node_name = data["starting_node_name"]
        return obj
