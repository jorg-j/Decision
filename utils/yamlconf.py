"""
Default Configure Yaml format
"""

import yaml


def readConfig(configFile):
    with open(configFile) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # transform json into object
    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    returnData = Struct(**data)

    return returnData


def writeConfig(configFile, data):
    with open(configFile, "w") as file:
        documents = yaml.dump(data, file, explicit_start=True)