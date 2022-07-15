
def remap_columns(df, data):
    """
    The function takes a dataframe and a dictionary as arguments. The dictionary contains the column
    names and the mapping data. The function then maps the data to the columns

    :param df: The dataframe that you want to remap
    :param data: The dataframe that contains the columns to be remapped
    """
    remap_cols = data["Columns"]

    for col in remap_cols:
        # Mapping the data to the columns.
        d = data[col]
        df[col] = df[col].map(d)