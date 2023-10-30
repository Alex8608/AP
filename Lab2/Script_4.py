import pandas as pd
import datetime as dt
from os import listdir


def find_in_dataset(date:dt.datetime) -> str:
    """Return course of dollar from dataset.csv"""
    dataset=pd.read_csv("./Lab1/dataset.csv", names=["Date", "Course"])
    try:
        return dataset[dataset.Date==date.isoformat()[:10]].Course.item()
    except:
        return None

def find_in_X_Y(date:dt.datetime) -> str:
    """Return course of dollar from X.csv and Y.csv"""
    X=pd.read_csv("./Lab2/X.csv", names=["Date"])
    Y=pd.read_csv("./Lab2/Y.csv", names=["Course"])
    try:
        return Y.at[X[X.Date==date.isoformat()[:10]].Date.index[0], "Course"]
    except:
        return None
    
def find_in_years(date:dt.datetime) -> str:
    for name in listdir("./Lab2/Years"):
        if name[:4]==date.isoformat()[:4]:
            file=pd.read_csv(f'./Lab2/Years/{name}', names=["Date","Course"])
            try:
                return file[file.Date==date.isoformat()[:10]].Course.item()
            except:
                return None
    return None

def find_in_weeks(date:dt.datetime) -> str:
    for name in listdir("./Lab2/Weeks"):
        if dt.datetime(int(name[:4]),int(name[4:6]),int(name[6:8]))<=date<=dt.datetime(int(name[9:13]),int(name[13:15]),int(name[15:17])):
            file=pd.read_csv(f'./Lab2/Weeks/{name}', names=["Date","Course"])
            try:
                return file[file.Date==date.isoformat()[:10]].Course.item()
            except:
                return None
    return None

if __name__=="__main__":
    input_date=dt.datetime.strptime(str(input()),"%d/%m/%y")
    print(find_in_dataset(input_date))
    print(find_in_X_Y(input_date))
    print(find_in_years(input_date))
    print(find_in_weeks(input_date))
