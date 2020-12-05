import time

import eel
from src.ActionNetwork.ActionNetwork import ActionNetwork
from src.Actions.ActionProfileManager import ActionProfileManager

@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


@eel.expose
def test_alerts():
    time.sleep(1)
    eel.alert_client("alert 0")
    print('alert 1')
    time.sleep(1)
    eel.alert_client("alert 1")
    print('alert 2')
    return
# eel.say_hello_js('Python World!')   # Call a Javascript function
