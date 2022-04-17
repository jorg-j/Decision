# sudo apt-get install libatlas-base-dev
# sudo apt-get install graphviz
import json
import pickle

import pandas

from utils import monkey
from utils.reclassify import restore
from utils.yamlconf import readConfig
from utils.jsontools import ReadJson


def read_model():
    """
    It reads the model from the file `data/model.pk` and returns it
    :return: A dictionary of dictionaries.
    """
    with open("data/model.pk", "rb") as f:
        datatree = pickle.load(f)
    return datatree

def remap(config, dataframe, data):
    """
    :param config: The configuration file
    :param dataframe: the dataframe you want to remap
    :param data: a dictionary containing the data to be mapped
    """
    for col in data["Columns"]:
        if col != config.data["result"]:
            d = data[col]
            dataframe[col] = dataframe[col].map(d)

def main():

    # Import the user config
    config = readConfig("data/config.yml")

    # Import the mapped data
    data = ReadJson(file="data/mapped.json")
    
    # Generate dataframe from input file
    df = pandas.read_csv(config.input)

    # Remap the dataframe against the mapped data.
    remap(config, df, data)

    # Define the feature columns
    features = config.data["features"]

    # Assign the feature columns to X
    X = df[features]

    # Import the model
    dtree = read_model()

    # Determine the outcome as an integer
    outcome = dtree.predict(X)[0]

    # Restore the outcome to match the result value
    final_result = restore(config.data["result"], outcome)

    print(final_result)




if __name__ == "__main__":
    config = readConfig("data/config.yml")
    watch = monkey.Monkey(config.input)

    while True:
        if watch.run:
            main()

        watch.ook()
