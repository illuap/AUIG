from actionProfile import *


def getAllNodes():
    dataSet = []

    for index, (key, value) in enumerate(ActionProfiles.items()):
        if (index == 0):
            dataSet.append({"id": key, "label": key, "color": 'lime'})
        else:
            dataSet.append({"id": key, "label": key})

    return dataSet


def getAllEdges():
    dataSet = []

    for index, (key, value) in enumerate(ActionProfiles.items()):
        for index2, (key2, value2) in enumerate(ActionProfiles[key]["edges"].items()):
            dataSet.append({"from": key, "to": value2, "label": key2, "arrows": 'to'})

    return dataSet
