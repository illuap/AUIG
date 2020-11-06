from configmanager import config
from screengrabber import ScreenGrabberWin32
from action import *

from enums.actionTypes import actionTypes
from enums.actionStatusTypes import actionStatusTypes
from actionProfile import *
from actionNetwork import *


import actionProfileToGraph

print(actionProfileToGraph.getAllNodes())
print(actionProfileToGraph.getAllEdges())

import eelMain

## RECURSIVE LOOP BECAUSE I USED A TREE FOR A FSM lul
# from treantActionProfileParser import *
# print(getTreantNodeStructureJSON(actionProfile("open_missions")))

print(config['APPNAME'])

#aP = actionProfile("test")
#dog = actionProfile("insert", actionTypes.CHECK_AND_CLICK.name, {actionStatusTypes.ACTION_DONE.name: "uniqueNameHere"}, {})
#dog.save()

#SG = ScreenGrabberWin32(config["APPNAME"])
#SG.getScreenShot()


#an = actionNetwork(SG)




