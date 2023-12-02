import pandas as pd
import datetime as dt
from os import listdir


def find_in_dataset(date:str, path:str) -> str:
    """Return course of dollar from dataset.csv"""
    dataset=pd.read_csv(path, names=["Date", "Course"])
    try:
        return dataset[dataset.Date==date].Course.item()
    except:
        return None