import numpy as np

print("Value Types:", "1 - Median", "2 - Mean", "3 - Max", "4 - Min", "5 - Std Dev", "0 - All types")


value = input("Enter desired value type(s): ") #needs to be tuple/array of ints1
value = list(map(int, value.split()))

print(value)

#make dictionary, keys as cases, do a try except statement
#(as long as all functions act on the same value )
#if iterating through a list, for loop through the try function
match value: #need to make it to where multiple inputs at once are read
    case value if 1 in value:
        print(1)
            
    case value if 2 in value:
        print(2)
            
    case value if 3 in value:
        print(3)

    case value if 4 in value:
        print(4)

    case value if 5 in value:
        print(5)

    case value if 0 in value:
        print(0)

    case _:
        print("Invalid")


