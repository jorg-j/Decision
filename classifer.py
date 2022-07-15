# sudo apt-get install libatlas-base-dev
# sudo apt-get install graphviz

import pickle

import pandas
from utils.reclassify import restore
from utils.jsontools import ReadJson


def read_model():
    """
    It reads the model from the file `data/model.pk` and returns it
    :return: A dictionary of dictionaries.
    """
    with open("data/model/model.pk", "rb") as f:
        datatree = pickle.load(f)
    return datatree


def remap(dataframe, data):
    """
    :param config: The configuration file
    :param dataframe: the dataframe you want to remap
    :param data: a dictionary containing the data to be mapped
    """
    for col in data["Columns"]:
        if col != "Result":
            d = data[col]
            dataframe[col] = dataframe[col].map(d)


def main():
    # Import the user config
    # config = readConfig("data/config.yml")

    # Import the mapped data
    data = ReadJson(file="data/model/mapped.json")

    # Generate dataframe from input file
    df = pandas.read_csv("data/new.csv")

    df_output = pandas.read_csv("data/new.csv")

    # Remap the dataframe against the mapped data.
    remap(df, data)

    # Define the feature columns
    features = df.columns.values

    # Assign the feature columns to X
    X = df[features]

    # Import the model
    dtree = read_model()

    # Determine the rowcount and start new collection
    rowcount = df.shape[0]
    outcomes = []

    for i in range(rowcount):
        # Determine the outcome as an integer
        outcome = dtree.predict(X)[i]

        # Restore the outcome to match the result value
        final_result = restore("Result", outcome)
        outcomes.append(final_result)

    # Create Results Column
    df_output["Results"] = outcomes
    df_output.to_csv(path_or_buf="data/results.csv", index=False)


if __name__ == "__main__":
    main()
