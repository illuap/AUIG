import eel

from src.WebApp.AUIG_WebApp import  AUIRG_WebApp

#technically abandoned?

@eel.expose  # Expose this function to Javascript
def get_(x):
    print('Hello from %s' % x)


@eel.expose
def show_actions_in_action_network():
    print('hello')
    app: AUIRG_WebApp = AUIRG_WebApp()

    print(app)
    print(type(app))
    info = app.aNetwork.getActionsInNetwork()

    eel.popup_client(info)
    return
