import pandas as pd

dataset=pd.read_csv("./Lab1/dataset.csv", header=None)
dataset[0]=pd.to_datetime(dataset[0])
dataset=dataset.sort_values(by=0)

def next() -> str:
    """Return first and next data"""
    global dataset
    while not dataset.empty:
        data=dataset.iloc[0]
        dataset=dataset.iloc[1:]
        return (data[0].isoformat()[:10],data[1])
    return None

if __name__=="__main__":
    print(next())
    print(next())
    print(next())