# sudo apt-get install libatlas-base-dev
# sudo apt-get install graphviz
import json

import pickle

import pandas

from utils.reclassify import restore
from utils.yamlconf import readConfig

config = readConfig("data/config.yml")

df = pandas.read_csv(config.input)

with open('data/mapped.json', 'r')as jsonfile:
    data = json.load(jsonfile)

remap_cols = data['Columns']

for col in remap_cols:
    if col != config.data['result']:
        d = data[col]
        df[col] = df[col].map(d)

features = config.data['features']

X = df[features]

with open('data/model.pk', 'rb')as f:
    dtree = pickle.load(f)

outcome = dtree.predict(X)[0]

final_result = restore(config.data['result'], outcome)

print(final_result)