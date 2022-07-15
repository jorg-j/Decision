import pandas as pd

from sklearn import metrics
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier

from utils.estimator import define_params
from utils.modelTools import write_model
from utils.plotters import save_tree
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


X = df[feature_cols]  # Features
y = df.Result  # Target variable


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)

# Grid Search the data to define the best possible parameters for the model
params = define_params(X_train, y_train)


# Create Decision Tree classifer object
clf = DecisionTreeClassifier(
    criterion=params.get("criterion"),
    max_depth=params.get("max_depth"),
    max_features=params.get("max_features"),
    splitter=params.get("splitter"),
)

# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)


# Predict the response for test dataset
y_pred = clf.predict(X_test)


print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


# Save the tree PNG to data/tree.png
save_tree(model=clf, feature_cols=feature_cols)

write_model(clf)
