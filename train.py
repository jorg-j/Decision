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


config = readConfig("data/config.yml")

df = pandas.read_csv(config.source)

print(df)

if not os.path.exists('data/mapped.json'):
    unique(df)

with open('data/mapped.json', 'r')as jsonfile:
    data = json.load(jsonfile)



remap_cols = data['Columns']

for col in remap_cols:
    d = data[col]
    df[col] = df[col].map(d)


features = config.data['features']
result = config.data['result']

X = df[features]
y = df[result]

dtree = DecisionTreeClassifier()
dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('data/decisiontree.png')

with open('data/model.pk', 'wb')as f:
    pickle.dump(dtree, f)