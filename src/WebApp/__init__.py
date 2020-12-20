import eel

from .EelAPI import *



def startApp():
    eel.init('static_web')
    eel.start('templates/actionProfiles/actionProfilePage.html', size=(600, 980), jinja_templates='templates', disable_cache=True)  # Start