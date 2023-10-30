import pandas as pd

class DatasetIterator:
    def __init__(self, name):
        self.dataset=pd.read_csv(name, header=None)
        self.dataset[0]=pd.to_datetime(self.dataset[0])
        self.dataset=self.dataset.sort_values(by=0)

    def __iter__(self):
        return self
    
    def __next__(self):
        while not self.dataset.empty:
            data=self.dataset.iloc[0]
            self.dataset=self.dataset.iloc[1:]
            return (data[0].isoformat()[:10],data[1])
        raise StopIteration

if __name__=="__main__":
    data=DatasetIterator("./Lab1/dataset.csv")
    for i in data:
        print(i)