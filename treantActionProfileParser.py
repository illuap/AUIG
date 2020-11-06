from actionProfile import *

def getTreantNodeJSON(actionProfile):
    # text = {"uniqueName": actionProfile.uniqueName, 
    #         "actionType": actionProfile.actionType,
    #         "startDelay": actionProfile.delays["START_DELAY"], 
    #         "postDelay": actionProfile.delays["POST_DELAY"], }
    text = actionProfile.getJsonData()

    img = "" + actionProfile.data["img1"]

    return {"text":text, "image":img}

def getTreantNodeStructureJSON(headNode):

    text = getTreantNodeJSON(headNode)

    children = []

    for index, (key, value) in enumerate(headNode.edges.items()):
        subtext = getTreantNodeStructureJSON(actionProfile(value))
        children.append(subtext)


    text["children"] = children

    return text