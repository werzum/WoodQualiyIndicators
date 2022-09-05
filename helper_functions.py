import pandas as pd

def import_file(path):
    with open(path) as file:
        table = pd.read_csv(file)
    return table