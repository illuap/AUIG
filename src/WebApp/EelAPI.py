import eel

from src.WebApp.AUIG_WebApp import  AUIRG_WebApp
from src.Tools.AppCheckerTool import AppCheckerTool
from src.Tools.ProfileViewer import ProfileViewer

#technically abandoned?

@eel.expose  # Expose this function to Javascript
def get_(x):
    print('Hello from %s' % x)


@eel.expose
def show_actions_in_action_network():
    app: AUIRG_WebApp = AUIRG_WebApp.get_instance()

    print(app)
    print(type(app))
    info = app.aNetwork.getActionsInNetwork()

    eel.popup_client(info)
    return

@eel.expose
def focus_nox_window():
    AppCheckerTool.FocusNox()
    return

@eel.expose
def start_action_network():
    app: AUIRG_WebApp = AUIRG_WebApp.get_instance()
    app.aNetwork.traverseNetwork()

@eel.expose
def get_all_profiles():
    return ProfileViewer.GetAllProfiles()

@eel.expose
def set_profile(profile_name):
    fileDir = ProfileViewer.GetFileDirForDataFile(profile_name)

    app: AUIRG_WebApp = AUIRG_WebApp.get_instance()
    app.apManager.setJsonFile(fileDir)

    # TODO: success or failure notification
    # return success
    # else return error
    return fileDir