import matplotlib.pyplot as plt
import os.path
from os import path
import csv
import pandas as pd

def gold_price_plot(condition):

    try:
        f = open('gold_price_data.csv')
        f.close()

    except FileNotFoundError:
        print("File not exist")


    x = []
    y = []
    df = pd.read_csv('gold_price_data.csv')
    df = df.groupby(by=df['time']).mean().reset_index()
    dfmax = df.groupby(by=df['time']).max().reset_index()
    dfmin = df.groupby(by=df['time']).min().reset_index()

    if condition == "avg":
        df.plot(kind="line",x='time',y='price')
        plt.show()
    if condition == "max":
        dfmax.plot(kind="line",x='time',y='price',color='red')
        plt.show()
    if condition == "min":
        dfmin.plot(kind="line",x='time',y='price',color='blue')
        plt.show()





