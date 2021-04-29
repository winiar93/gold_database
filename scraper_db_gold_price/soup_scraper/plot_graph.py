import matplotlib.pyplot as plt
import os.path
import csv
import pandas as pd

def gold_price_plot(condition):

    if os.path.isfile('gold_price_data.csv'):
        print("File exist")
    else:
        print("File not exist")
    print("number of lines in file :")
    print(sum(1 for line in open('gold_price_data.csv')))

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




if __name__ == '__main__':
    gold_price_plot("max")

