import pandas as pd

def split_by_columns(filepath:str, path:str) -> None:
    dataset=pd.read_csv(filepath, header=None)
    """Split by columns and write to file"""
    dataset[0].to_csv(f"{path}/X.csv", index=None, header=None)
    dataset[1].to_csv(f"{path}/Y.csv", index=None, header=None)