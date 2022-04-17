import json


def ReadJson(file):
    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
    return data