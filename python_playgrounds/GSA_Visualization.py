from generalizedStockAnalysis import d_ticker
import matplotlib.pyplot as plt


#provide choice for plot axis designation
print("a: Plot against time")
print("b: Plot against other")
choice = input("Enter a or b:")


#plotting data to determine certain patterns
def plot_time():
    key_y = input("Enter desired ticker for yvals:")
    val_y = input('Enter category (Close, Open, etc.) for yvals:')
    yvals = d_ticker[key_y][val_y]
    xvals = d_ticker[key_y]['Date']


    plt.plot(xvals, yvals)
    plt.xlabel(f"{xvals[0]} - {xvals[len(xvals)-1]}")
    plt.ylabel(f"{val_y}")
    plt.title(f"{key_y} {val_y} vs. Time")
    plt.show()


def plot_other():
    key_x = input("Enter desired ticker for xvals:")
    val_x = input('Enter category (Close, Open, etc.) for xvals:')
    key_y = input("Enter desired ticker for yvals:")
    val_y = input('Enter category (Close, Open, etc.) for yvals:')

    xvals = d_ticker[key_x][val_x]
    yvals = d_ticker[key_y][val_y]

    plt.plot(xvals, yvals)
    plt.xlabel(f"{key_x} {val_x}")
    plt.ylabel(f"{key_y} {val_y}")
    plt.title(f"{key_y} {val_y} vs. {key_x} {val_x}")
    plt.show()


match choice: #calls plot function depending on what type of plot is wanted
    case 'a':
        plot_time()
    
    case 'b':
        plot_other()

    case _:
        print("invalid")



