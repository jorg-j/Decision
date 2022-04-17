import pickle


def WriteModel(decision_tree):
    """
    > The function takes a decision tree object as input and writes it to a file called `model.pk` in
    the `data` folder
    
    :param decision_tree: The decision tree model
    """
    # Write the model
    with open('data/model.pk', 'wb')as f:
        pickle.dump(decision_tree, f)