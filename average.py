#Author: Soorya Pandian
def average(*arg:int):
    """Given number of integers, this function will calculate their average"""
    count=len(arg)
    num=0
    for i in arg:
        num+=i
    return num/count
print("The average of the numbers is:",average(10,20,60))

