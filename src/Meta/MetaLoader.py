import os
from typing import Dict

import jsonpickle

from loguru import logger
from src.Meta.Models.ActionProfileMetaModel import ActionProfileMetaModel


class MetaLoader:
    __data = None
    __stale_data = True
    file_name: str
    parent_dir: str

    def __init__(self, dir):
        self.parent_dir, file = os.path.split(dir)
        self.parent_dir = self.parent_dir + "/"
        self.file_name, ext = os.path.splitext(file)

        self.__data = self.get_data()

    def get_file_path(self):
        return self.parent_dir + self.file_name + "_meta.json"

    def save_metadata(self):
        path_access = 'w+'
        if os.path.exists(self.get_file_path()):
            path_access = 'w'
        with open(self.get_file_path(), path_access) as f:
            jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
            f.write(jsonpickle.encode(self.__data, unpicklable=False))

    def set_data(self, data):
        try:
            self.__data = data

            temp = jsonpickle.encode(self.__data, unpicklable=False)
            temp2 = jsonpickle.decode(temp)
            self.save_metadata()
            self.__stale_data = True
            logger.info("saved new meta data.")
        except Exception as e:
            logger.warning("Could not set the meta data " + self.parent_dir + self.file_name)

    def get_data(self) -> Dict:
        if self.__stale_data:
            if (not os.path.exists(self.get_file_path())):
                self.set_data("{}")
            with open(self.get_file_path(), "r") as f:
                self.__data = jsonpickle.decode(f.read())
                logger.info("fetching new meta data.")

        return self.__data
