import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype
def seperation(df):
    cols = df.columns
    rows = df.shape[0]
    idx = []
    categorical = []
    continous = []
    for var in cols:
        if is_string_dtype(df[var]):
            categorical.append(var)
        elif len(df[var].unique())/float(rows) <= 0.05 and is_numeric_dtype(df[var]) :
            categorical.append(var)
        elif len(df[var].unique()) == rows:
            idx.append(var)
        else:
            continous.append(var)
    return idx, categorical, continous