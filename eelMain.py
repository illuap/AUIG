import eel, os, random
import json
import re
from enums.actionTypes import actionTypes
from actionProfile import ActionProfiles, actionProfile
import os
from screengrabber import ScreenGrabberWin32
from configmanager import config
from actionNetwork import actionNetwork
from helper import *

path = 'c:\\projects\\hc2\\' # TODO change this 

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        #if '.txt' in file:
        files.append(os.path.join(r, file))

print("-= INITIAL LOAD =-")
SG = ScreenGrabberWin32(config["APPNAME"])
SG.getScreenShot()
    
print("===="+config["APPNAME"])
#an = actionNetwork(SG)


eel.init('web')

@eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'

#GIVE
@eel.expose
def get_all_actions():
    print([i.name for i in actionTypes])
    return([i.name for i in actionTypes])
#GIVE 
@eel.expose
def get_all_image_dirs():
    rootDir = "./web/images/"

    imgDirs = []

    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)

        for fname in fileList:
            joined = os.path.join(dirName,fname)
            formatted = re.sub(r'/|\\', re.escape(os.sep), joined)
            formatted=formatted[5:] #removes '.\\web'
            print('\t%s' % formatted)
            imgDirs.append(formatted)
    return(imgDirs)

@eel.expose
def get_all_nodes():
    return(list(ActionProfiles.keys()))

@eel.expose
def save_action_entry(jsonData):
    print(jsonData)
    
    #fix the image directory name to save.
    for k in jsonData["data"].keys():
        if("img" in k):
            new = convertJStoPYFileName(jsonData["data"][k])
            jsonData["data"][k] = new

    entry = actionProfile(jsonData["uniquename"], jsonData["actiontype"], jsonData["edges"], jsonData["data"],jsonData["delays"])
    entry.save()


print(get_all_nodes())

@eel.expose
def start_actions():
    
    SG = ScreenGrabberWin32(config["APPNAME"])
    SG.getScreenShot()
    
    print("===="+config["APPNAME"])
    an = actionNetwork(SG)

@eel.expose
def getStartingNodeName():
    # convert dictionary to iterator and get the first value
    return next(iter(ActionProfiles.keys()))
0
## LIST OF IMAGES

#SET
## IMAGE
## LINKING


eel.start('templates/index.html.j2', size=(900, 1000), jinja_templates='templates')
