import pandas as pd

dataset=pd.read_csv("./Lab1/dataset.csv", header=None)
dataset=dataset.sort_values(by=0)

def split_by_years(data:pd.DataFrame) -> dict:
    """Split by years"""
    d={}
    for i in range(len(dataset[0])):
        if dataset[0][i][:4] not in d:
            d[dataset[0][i][:4]]=[]
        d[dataset[0][i][:4]].append(f'{dataset[0][i]},{dataset[1][i]}')
    return d
def write_to_file(d:dict) -> None:
    """Write to file"""
    for k in d:
        file=open(f'./Lab2/Years/{d[k][len(d[k])-1].replace("-","").replace(",","")[:8]}_{d[k][0].replace("-","").replace(",","")[:8]}.csv','w')
        for i in range(len(d[k])):
            file.write(d[k][i]+"\n")
        file.close()

if __name__=="__main__":
    write_to_file(split_by_years(dataset))