import json


def WriteJson(file, data):
    """
    > The function takes a file name and a data structure as input, and writes the data structure to the
    file in JSON format
    
    :param file: The file to write to
    :param data: The data to be written to the file
    """
    with open(file, "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


def ReadJson(file):
    """
    It opens the file, reads the file, and then closes the file
    
    :param file: The file to read
    :return: A dictionary
    """
    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
    return data

def class_names():
    """
    It reads the json file, gets the values, and then returns the keys that correspond to those values
    :return: A list of the class names
    """
    data = ReadJson('data/model/mapped.json')
    vals = []
    reverse_map = data.get('Result')

    for i in range(len(reverse_map.items())):
        for k, v in reverse_map.items():
            if v == i:
                vals.append(k)
    return vals