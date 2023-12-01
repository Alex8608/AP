import pandas as pd

def split_by_columns(filepath:str) -> None:
    dataset=pd.read_csv(filepath, header=None)
    """Split by columns and write to file"""
    dataset[0].to_csv("./Lab2/X.csv", index=None, header=None)
    dataset[1].to_csv("./Lab2/Y.csv", index=None, header=None)

if __name__=="__main__":
    split_by_columns("./Lab1/dataset.csv")