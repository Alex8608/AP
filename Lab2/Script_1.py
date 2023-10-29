import pandas as pd

if __name__=="__main__":
    dataset=pd.read_csv("./Lab1/dataset.csv", header=None)
    dataset[0].to_csv("./Lab2/X.csv", index=None, header=None)
    dataset[1].to_csv("./Lab2/Y.csv", index=None, header=None)