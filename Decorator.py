#Author : Soorya Pandian 
from datetime import datetime
def write_log(filename,log_message,log_level="INFO"):
    """Given filepath, message and log info, this function writes logfile in desired location"""
    try:
        current_time=datetime.now()
        current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry=f'[{current_time}] {[log_message]} {log_level}\n'
        with open(filename,"a")as log_file:
            log_file.write(log_entry)
    except Exception as e:
        print(f"Faied to write log : {e}")

import time
def clocking(func_pointer):
    """Decorator which will clock the function"""
    def innerfunc(*arg,**kwds):
        start_time=time.time()
        i=func_pointer(*arg,**kwds)
        end_time=time.time()
        total=end_time-start_time
        return total,i
    return innerfunc

def logfile(func_pointer):
    """Decorator to prompt the log writing function"""
    def innerfunc(*arg,**kwds):
        write_log(r'A:\text.txt',"Function started")
        total,average=func_pointer(*arg,**kwds)
        write_log(r'A:\text.txt',"Function end")
        write_log(r'A:\text.txt',f'Function execution time is {total} seconds')
        return average
    return innerfunc

@logfile
@clocking
def average(*arg:int):
    """Given number of integers, this function will calculate their average"""
    num=sum(i for i in arg)
    return num/len(arg)
print("The average of the numbers is:",average(1, 2, 3, 29, -10) + average(1, 2))

 
