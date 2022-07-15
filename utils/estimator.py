from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

from utils.jsontools import WriteJson


def define_params(X_train, y_train):
    """
    It takes in the training data and the training labels, and then it uses GridSearchCV to find the
    best parameters for the DecisionTreeClassifier
    
    :param X_train: The training data
    :param y_train: The training labels
    :return: The best parameters for the decision tree classifier.
    """

    params = {
        "criterion": ["gini", "entropy"],
        "max_depth": [None, 2, 4, 6, 8, 10, 12],
        "max_features": [None, "sqrt", "log2", 0.2, 0.4, 0.6, 0.8],
        "splitter": ["best", "random"],
    }

    clf = GridSearchCV(
        estimator=DecisionTreeClassifier(),
        param_grid=params,
        cv=5,
        n_jobs=5,
        verbose=1,
    )

    clf.fit(X_train, y_train)

    print(clf.best_params_)

    WriteJson(file="data/model/params.json", data=clf.best_params_)

    return clf.best_params_
