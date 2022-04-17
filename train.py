# sudo apt-get install libatlas-base-dev
# sudo apt-get install graphviz
import json
import os
import pickle

import pandas
import pydotplus
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

from utils.reclassify import unique
from utils.yamlconf import readConfig
from utils.jsontools import ReadJson
from utils.modelTools import WriteModel

def remap_columns(df, data):
    """
    The function takes a dataframe and a dictionary as arguments. The dictionary contains the column
    names and the mapping data. The function then maps the data to the columns
    
    :param df: The dataframe that you want to remap
    :param data: The dataframe that contains the columns to be remapped
    """
    remap_cols = data['Columns']

    for col in remap_cols:
        # Mapping the data to the columns.
        d = data[col]
        df[col] = df[col].map(d)

def generate_decision_img(features, decision_tree):
    """
    It takes the features and the decision tree and generates a png image of the decision tree
    
    :param features: the names of the features in the dataset
    :param decision_tree: The decision tree object that we created in the previous step
    """
    data = tree.export_graphviz(decision_tree, out_file=None, feature_names=features)
    graph = pydotplus.graph_from_dot_data(data)
    graph.write_png('data/decisiontree.png')

config = readConfig("data/config.yml")

df = pandas.read_csv(config.source)

print(df)

# If the mapped json is missing then rebuild it
if not os.path.exists('data/mapped.json'):
    unique(df)

data = ReadJson('data/mapped.json')

# Remap strings to ints based on the mapped.json
remap_columns(df, data)

# Define the features and result from the user config
features = config.data['features']
result = config.data['result']

# Declare the feature data against the expected results
X = df[features]
y = df[result]

# Run the decision Classifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X, y)

# Generate decision tree image
generate_decision_img(features, decision_tree)

WriteModel(decision_tree)