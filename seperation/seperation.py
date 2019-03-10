import pandas as pd

def seperation(df):
    cols = df.columns
    rows = df.shape[0]
    idx = []
    categorical = []
    continous = []
    for var in cols:
        if len(df[var].unique())/float(rows) <= 0.05:
            categorical.append(var)
        elif len(df[var].unique()) == rows:
            idx.append(var)
        else:
            continous.append(var)
    return idx, categorical, continous