import pandas as pd
import numpy as np
import datetime as dt

def NormalDataset(dataset:pd.DataFrame)->pd.DataFrame:
    '''Убираем NaN, добавляем медиану и ср знач'''
    dataset.replace("None",pd.NaT)
    dataset.dropna(inplace=True, ignore_index=True)
    """До 1998 был советский рубль который в 1000 раз меньше современного"""
    for i in range(len(dataset["Date"])):
        if dataset["Date"][i][:4] in map(str,range(1992,1998)):
            dataset.loc[i,"Course"]/=1000
    median=dataset["Course"].median()
    mean=dataset["Course"].mean()
    print(median)
    print(mean)
    dataset["Relative_median"]=dataset.apply(lambda row: abs(row["Course"]-median),axis=1)
    dataset["Relative_mean"]=dataset.apply(lambda row: abs(row["Course"]-mean),axis=1)
    dataset = dataset.sort_values(by="Date", ignore_index=True)
    return dataset

def FindCourseRelativeMean(dataset:pd.DataFrame, value:float)->pd.DataFrame:
    '''Возвращает датасет в котором, значение отклонения от курса >= заданного значения'''
    return dataset.query('Relative_mean >= @value')

def FindCourseInTimeInterval(dataset:pd.DataFrame, first_date:dt.date, last_date:dt.date)->pd.DataFrame:
    '''Возвращает датасет в котором, дата удовлетворяет начальная дата <= дата <= конечная дата'''
    return dataset.query('Date >= @first_date and Date <= @last_date')

def GroupByMonth(dataset:pd.DataFrame)->pd.DataFrame:
    dataset['Date'] = pd.to_datetime(dataset['Date'], errors='coerce')
    return dataset.groupby([(dataset["Date"].dt.year), (dataset["Date"].dt.month)]).mean()

if __name__=="__main__":
    dataset=pd.read_csv("./Lab1/dataset.csv", header=None, names=["Date", "Course"])
    print(dataset)
    dataset=NormalDataset(dataset)
    print(dataset)
    #dataset=FindCourseRelativeMean(dataset,40.0)
    print(FindCourseRelativeMean(dataset,40.0))
    #dataset=FindCourseInTimeInterval(dataset, "2020-01-01", "2023-01-01")
    print(FindCourseInTimeInterval(dataset, "2020-01-01", "2023-01-01"))
    #dataset=GroupByMonth(dataset)
    print(GroupByMonth(dataset))