import pandas as pd
from os import mkdir
from os.path import exists

def split_by_year(dataset:pd.DataFrame) -> dict:
    """Split by years"""
    d={}
    for i in range(len(dataset[0])):
        if dataset[0][i][:4] not in d:
            d[dataset[0][i][:4]]=[]
        d[dataset[0][i][:4]].append(f'{dataset[0][i]},{dataset[1][i]}')
    return d

def split_by_years(filepath:str, path:str) -> None:
    """Write to file"""
    dataset=pd.read_csv(filepath, header=None)
    dataset=dataset.sort_values(by=0)
    d=split_by_year(dataset)
    if not exists(f"{path}/Years"):
        mkdir(f"{path}/Years")
    for k in d:
        file=open(f'{path}/Years/{d[k][len(d[k])-1].replace("-","").replace(",","")[:8]}_{d[k][0].replace("-","").replace(",","")[:8]}.csv','w')
        for i in range(len(d[k])):
            file.write(d[k][i]+"\n")
        file.close()