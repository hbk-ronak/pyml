import pandas as pd
from seperation import seperation
import missing
def imputation(data, scheme = 'auto'):
    idx, categorical, continous = seperation.seperation(data)
    missed = missing.missing_values_table(data)
    imputed_with = {}
    if scheme == 'auto':
        for var in missed:
            data[var+"_imputed"] = data[var].isna().apply(lambda x: 1 if x else 0)
            if var in categorical:
                data[var] = data[var].fillna("NA")
                imputed_with[var] = "NA" 
            if var in continous:
                vals = data[var].median()
                data[var] = data[var].fillna(vals)
                imputed_with[var] = vals
    else:
        imputed_with = scheme
        for key in scheme:
            data[key+"_imputed"] = data[key].isna().apply(lambda x: 1 if x else 0)
            data[key] = data[key].fillna(scheme[key])
    return data, imputed_with