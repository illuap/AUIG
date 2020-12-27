import os

from typing import Dict

import jsonpickle

from src.Actions.Models.ActionProfileMetaModel import ActionProfileMetaModel


class ActionProfileMetaLoader:
    data: ActionProfileMetaModel
    parent_profile_name: str
    parent_dir: str

    def __init__(self, dir):
        self.parent_dir, file = os.path.split(dir)
        self.parent_profile_name, ext = os.path.splitext(file)

    def get_file_path(self):
        return self.parent_dir + self.parent_profile_name + "_meta.json"

    def save_metadata(self):
        path_access = 'w+'
        if os.path.exists(self.get_file_path()):
            path_access = 'w'
        with open(self.get_file_path(), path_access) as f:
            jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
            f.write(jsonpickle.encode(self.data, unpicklable=False))
