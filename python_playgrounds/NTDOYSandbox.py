import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize as opt

'''
start with CRANE exercises
use our own data and comments
overall learn the material better
'''

'''
import nintendo stocks (7/19/23 - 7/18/24)
skips column names
replaces dates with 000
'''
nintendo = np.genfromtxt("NTDOY.csv", skip_header= 0, missing_values= "nan",
                            filling_values= "000", delimiter = ",")


NTDOY_Open = nintendo[1:,1] #open vals (daily)
NTDOY_High = nintendo[1:,2] #high vals (daily)
NTDOY_Low = nintendo[1:,3] #low vals (daily)
NTDOY_Close = nintendo[1:,4] #close vals (daily)
NTDOY_AdjClose = nintendo[1:,5] #adjusted close vals (daily)
NTDOY_Vol = nintendo[1:,6] #volume vals (daily)


#x values for plotting
xvals = np.arange(1, len(NTDOY_Open)+1) #code date tate <3: how to do dates x-axis(easier than mpl)

'''
#opening vals plot
plt.plot(xvals, NTDOY_Open)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("opening Price")
plt.show()

#high vals plot
plt.plot(xvals, NTDOY_High)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("Daily High")
plt.show()

#low vals plot
plt.plot(xvals, NTDOY_Low)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("Daily Low")
plt.show()

#close vals plot
plt.plot(xvals, NTDOY_Close)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("Closing Price")
plt.show()

#adj. close vals plot
plt.plot(xvals, NTDOY_AdjClose)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("Adj. Closing Price")
plt.show()

#vol vals plot
plt.plot(xvals, NTDOY_Vol)
plt.xlabel("days (7/19/23 - 7/18/24)")
plt.ylabel("Daily Volume")
plt.show()
'''

#test relation between different values
plt.subplot(2,2,1)
plt.plot(NTDOY_Open, NTDOY_Close,'o', markersize = 1)
plt.xlabel("Opening Prices")
plt.ylabel("Closing Prices")
plt.title("Opening Price VS Closing Price")

plt.subplot(2,2,2)
plt.plot(NTDOY_High, NTDOY_Low,'o', markersize = 1)
plt.xlabel("High")
plt.ylabel("Low")
plt.title("High VS Low")

plt.subplot(2,2,3)
plt.plot(NTDOY_Vol, NTDOY_AdjClose)
plt.xlabel("Volume")
plt.ylabel("Adj Closing Price")
plt.title("Volume VS Adj Closing Price")

plt.subplot(2,2,4)
plt.plot(NTDOY_Open, NTDOY_Vol)
plt.xlabel("Opening Prices")
plt.ylabel("Volume")
plt.title("Opening Price VS Volume")

plt.show()
#use a disrt to fit data, don't know what, could just use gaussian for normal distr
#gonnna use a gaussian, will just piece together different gaussians
#or layover large scal, small scale gaussian bfs


def gaussian(a, x, x0, w):
    solution = a * np.exp(-(x - x0)**2/(2*w**2))

    return solution

