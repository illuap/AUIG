from enums.actionTypes import actionTypes
import json

actionProfileFileName = 'actionProfiles.json'
# make singleton?
if 'ActionProfiles' not in vars():
    with open(actionProfileFileName, 'r') as f:
        ActionProfiles = json.load(f)

DELAY_KEY = "delays"


class ActionProfileManager:
    # TODO fill in these functions
    # conversions
    def get_action_profile_from_json(self, json_data):
        pass

    def get_json_from_action_profile(self, action_profile):
        pass

    # db fetching
    def get_json_from_db(self, unique_name):
        pass

    def get_action_profile_from_db(self, unique_name):
        pass

    # db updates
    def save_action_profile_in_db(self, action):
        pass

    def update_action_profile_in_db(self, action):
        pass

    def delete_action_profile_in_db(self, unique_name):
        pass