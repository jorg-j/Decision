"""
Takes data/data.csv and creates a random forest model
This is exported to model.pk
"""
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split  # Import train_test_split function

from utils.modelTools import write_model
from utils.plotters import display_forest
from utils.reclassify import file_mapper
from utils.transformers import remap_columns

df = pd.read_csv("data/data.csv")

feature_cols = df.columns.values[:-1]

# Convert String to Ints
# This method is used over OneHotEncoder as we store the model at the end for re-use
# In this way we have a value map of what the values were encoded to.
data = file_mapper(df)

# Using the map of column values, action the remap
remap_columns(df, data)

# Determine the column name
columns = df.columns.values

# Manages missing data values by fitting mean values
imputer = SimpleImputer(missing_values=np.NaN, strategy="mean")
imputer = imputer.fit(df[columns])
df[columns] = imputer.transform(df[columns])


X = df[feature_cols]  # Features
y = df.Result  # Target variable


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)

forest = RandomForestClassifier(n_estimators=100, random_state=100)
forest.fit(X_train, y_train)

# Predict the response for test dataset
predictions = forest.predict(X_test)


print("Accuracy:", metrics.accuracy_score(y_test, predictions))

# Display the tree
display_forest(forest=forest, X=X)

# Save the tree
write_model(forest)
