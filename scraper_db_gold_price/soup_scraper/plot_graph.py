import matplotlib.pyplot as plt
import os.path

# def plot_price():
print(sum(1 for line in open('Output_gold.csv')))



if os.path.isfile('Output_gold.csv'):
    print ("File exist")
else:
    print ("File not exist")