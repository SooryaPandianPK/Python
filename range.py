#Author: Soorya Pandian
def myrange(start,end=None,step=1):
    """Given start,end and step count, this function gives a list of values within the range"""
    if end==None:
        end=start
        start=0
        
    if step==0:
        raise ValueError("Step cannot be zero")

    if step>0:
        while start<end:
            yield start
            start+=step
    elif step<0:    
        while start>end:
            yield start
            start+=step

print(list(myrange(10,50,10)))

    
