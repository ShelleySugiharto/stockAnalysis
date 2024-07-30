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


#provide downloaded data
fileName = input("Enter file name (not directory): ")


#note to self: need user intended start and end date, translate dates into array term (most efficient)
#cont'd: by row, 0 = 1st date recorded,,, len(data) - 1 = last date recorded
#cont'd: would mean dates would have to be read when parsed through because of differing 
#start and end dates in user input data


#call importantVals function using user input


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


#function takes file and finds its mean, median, max, min, and std deviation
#note to self: implement finding above vals in a certain time interval
#note to self: search up switch function in python -> might replace if elif body
#NTS: value might be a tuple, so might have to change 
def importantVals(file_name, startDate, endDate):

    fileDated = file_name[startDate, endDate]

    #user's desired value types
    print("Value Types:", "1 - Median", "2 - Mean", "3 - Max", "4 - Min", "5 - Std Dev", "0 - All types")
    value = input("Enter desired value type(s): ") #needs to be tuple/array of ints

    match value: #need to make it to where multiple inputs at once are read
        case 1:
            median = np.median(fileDated)
            return median
        
        case 2:
            mean = np.mean(fileDated)
            return mean
        
        case 3:
            maxVal = max(fileDated)
            return maxVal
        
        case 4:
            minVal = min(fileDated)
            return minVal
        
        case 5:
            stdDev = 0 #need to find std dev function np
            return stdDev
        
        case 0:
            allVals = [median, mean, maxVal, minVal, stdDev]
            return allVals
        
        case _:
            print("Invalid option")

    
