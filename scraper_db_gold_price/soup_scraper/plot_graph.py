import matplotlib.pyplot as plt
import os.path
import csv

def gold_price_plot():

    if os.path.isfile('Output_gold.csv'):
        print("File exist")
    else:
        print("File not exist")
    print("number of lines in file :")
    print(sum(1 for line in open('Output_gold.csv')))

    x = []
    y = []

    with open('Output_gold.csv','r') as sales_csv:
        plots = csv.reader(sales_csv, delimiter=',')
        for row in plots:
            x.append(row[1])
            y.append(row[2])

    plt.plot(x,y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    gold_price_plot()


