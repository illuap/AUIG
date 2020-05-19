from configmanager import config
from enums.actionTypes import actionTypes
from enums.actionStatusTypes import actionStatusTypes
from action import *
from actionProfile import *
import keyboard
import time

class actionNetwork:


    actionDic = {}
    

    def __init__(self, SG):
        allActions = ActionProfiles.keys()
        
        for name in allActions:
            ap = actionProfile(name)
            if(ap.actionType == actionTypes.FIND_AND_CLICK):
                self.actionDic[name] = findAndClickAct(SG, ap)
            elif(ap.actionType == actionTypes.CHECK_AND_CLICK):
                self.actionDic[name] = checkAndClickAct(SG, ap)

        #START
        currentAction = "open_missions"
        force_exit = False
        while(not keyboard.is_pressed('`') and not force_exit): #TODO check for key input to quit
            # execute any  start delays.
            if(self.actionDic[currentAction]._actionProfile.delays["START_DELAY"]):
                for i in range(0, int(self.actionDic[currentAction]._actionProfile.delays["START_DELAY"]*100)):
                    if(keyboard.is_pressed('`')):
                        force_exit = True
                        break
                    time.sleep(0.01)

            result = self.actionDic[currentAction].run()

            # execute any post delays.
            if(self.actionDic[currentAction]._actionProfile.delays["POST_DELAY"]):
                for i in range(0,int(self.actionDic[currentAction]._actionProfile.delays["POST_DELAY"]*100)):
                    if(keyboard.is_pressed('`')):
                        force_exit = True
                        break
                    time.sleep(0.01)


            print("Results: " + result.name)

            nextAction = ActionProfiles[currentAction]["edges"][result.name]
            currentAction = nextAction

        print("- Ending Action Network.")

            #if(result == actionStatusTypes.ACTION_DONE):
                # TODO implement get from profile next action and update currentAction
            #elif(result == actionStatusTypes.NO_ACTION_DONE):
                # TODO implement get from profile next action and update currentAction
            #TODO Write ENDCASE