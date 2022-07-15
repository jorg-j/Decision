import sys

import matplotlib.pyplot as plt
import pydotplus
import six
from IPython.display import Image
from sklearn.tree import export_graphviz, plot_tree

from utils.jsontools import class_names

sys.modules["sklearn.externals.six"] = six

def display_forest(forest, X):
    """
    It takes a trained random forest model and a dataframe of features, and displays the first tree in
    the forest
    
    :param forest: the forest object
    :param X: The dataframe of features
    """

    classNames = class_names()

    fig = plt.figure(figsize=(15, 10))
    plot_tree(forest.estimators_[0], 
            feature_names=X.columns,
            class_names=classNames, 
            filled=True, rounded=True)

    plt.show()



def save_tree(model, feature_cols):
    """
    It takes a trained decision tree model and a list of feature names, and saves a visualization of the
    tree to a PNG file
    
    :param model: the model you want to visualize
    :param feature_cols: The names of the columns that we're using to train the model
    """
    dot_data = six.StringIO()

    classNames = class_names()

    export_graphviz(
        model,
        out_file=dot_data,
        filled=True,
        rounded=True,
        special_characters=True,
        feature_names=feature_cols,
        class_names=classNames,
    )
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png("data/model/tree.png")
    Image(graph.create_png())
