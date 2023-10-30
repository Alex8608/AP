import pandas as pd
import datetime as dt

dataset=pd.read_csv("./Lab1/dataset.csv", header=None)
dataset[0]=pd.to_datetime(dataset[0])
dataset=dataset.sort_values(by=0)

def split_by_weeks(data:pd.DataFrame) -> list:
    """Split by weeks"""
    week_data=[]
    for week, group in dataset.set_index(0).groupby(pd.Grouper(freq='W')):
        week_data.append(group.apply(lambda x: [str(x.name)[:10], str(x[1])], axis=1).values.tolist())
    return week_data

def write_to_file(weeks:list) -> None:
    """Write to files"""
    for week in weeks:
        if week:
            file = open(f'./Lab2/Weeks/{week[0][0].replace("-","")}_{week[len(week)-1][0].replace("-","")}','w')
            for day in week:
                file.write(f'{day[0]},{day[1]}\n')
            file.close()

if __name__=="__main__":
    write_to_file(split_by_weeks(dataset))