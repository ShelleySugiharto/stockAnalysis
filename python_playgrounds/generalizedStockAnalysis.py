'''
generalized parser for any stock info from yahoo finance
divides data into 6 categories (in order):
- opening price
- daily high
- daily low
- closing price
- adj closing price
- daily volume

note to self: research monte carlo usage in stock analysis, try to figure out MC from CRANE lec

'''
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#type hints
def parser(file_name: str) -> list[np.array: int]:
    return list[np.array: int | str]

#provide downloaded data
fileName = input("Enter file name (not directory): ")


#note to self: need user intended start and end date, translate dates into array term (most efficient)
#cont'd: by row, 0 = 1st date recorded,,, len(data) - 1 = last date recorded
#cont'd: would mean dates would have to be read when parsed through because of differing 
#start and end dates in user input data


#function takes a file and parses through data, isolating into the 6 categories described in overall comment
def parser(file_name):
    data_Full = np.genfromtxt(file_name, delimiter = ',', skip_header = 0, 
                  missing_values= 'nan', filling_values = 'dates')
    
    data_Open = data_Full[:, 0]
    data_High = data_Full[:, 1]
    data_Low = data_Full[:, 2]
    data_Close = data_Full[:, 3]
    data_AdjClose = data_Full[:, 4]
    data_Vol = data_Full[:, 5]

    return data_Full, data_Open, data_High, data_Low, data_Close, data_AdjClose, data_Vol

#auto-plot function: enter what you want plotted using different data sets
def simplePlot(xvals, yvals, xlabel, ylabel, title):
    plt.plot(xvals, yvals)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

    


