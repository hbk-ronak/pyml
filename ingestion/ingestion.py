import zipfile as zp
import pandas as pd
from os import listdir
from os.path import isfile, join

def ingest(path):
    '''
    Loads data from a zip. The Zip should contain one train.csv file
    '''
    files = [f for f in listdir(path) if isfile(join(path, f)) if '.zip' in f]
    print(files)
    idx = input("Select the file(zero indexed): ")
    with zp.ZipFile(path+files[int(idx)]) as z:
        with z.open("train.csv") as f:
            df = pd.read_csv(f)
    n_rows, n_cols = df.shape
    logs = "The File contains: %i rows and %i columns" %(n_rows,n_cols)
    print(logs)
    return df