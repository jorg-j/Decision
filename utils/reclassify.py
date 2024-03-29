import pandas
import json



def unique(df):
    """
    It takes a dataframe, iterates through each column, and checks if the values in the column are all
    integers. If they are not, it creates a dictionary of the unique values in the column and their
    corresponding integer value. It then saves this dictionary to a json file.
    
    :param df: The dataframe you want to map
    """
    vals = {}
    map_col = []
    for col in df:
        try:
            values = [float(i) for i in df[col].unique()]
        except:
            values = [str(i) for i in df[col].unique()]

        is_int = all([isinstance(item, float) for item in values])

        if is_int == False:
            map_col.append(col)
            ints = [i for i in range(len(values))]
            remapped = {k: v for k, v in zip(values, ints)}
            vals[str(col)] = dict(remapped)

    vals['Columns'] = map_col

    with open('data/mapped.json', 'w') as outfile:
        json.dump(vals, outfile, indent=4, sort_keys=True)

def restore(ResultName, Value):
    """
    It takes a result name and a value, and returns the original value
    
    :param ResultName: The name of the result you want to restore
    :param Value: The value you want to convert to a string
    :return: The key of the value that is being passed in.
    """
    with open('data/mapped.json', 'r')as jsonfile:
        data = json.load(jsonfile)
    reverse_map = data.get(ResultName)
    for k, v in reverse_map.items():
        if v == Value:
            return k