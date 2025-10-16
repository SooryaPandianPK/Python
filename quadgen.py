#Author:Soorya Pandian
import random
def generate_random():
    """Calling this function would return three different random numbers"""
    alpha=random.uniform(0,1)
    beta=random.uniform(0,1-alpha)
    gamma=1-alpha-beta
    return alpha,beta,gamma

def quadcheck(a=[],b=[],c=[],d=[]):
    """Function to check the type of quad"""
    value1=(c[1] - a[1]) * (b[0] - c[0]) - (c[0] - a[0]) * (b[1] - c[1])
    value2=(c[1] - a[1]) * (d[0] - c[0]) - (c[0] - a[0]) * (d[1] - c[1])
    value3=(d[1] - b[1]) * (a[0] - d[0]) - (d[0] - b[0]) * (a[1] - d[1])
    value4=(d[1] - b[1]) * (c[0] - d[0]) - (d[0] - b[0]) * (c[1] - d[1])

    if value1*value2 > 0:
        return a,b,c,d
    elif value3*value4>0:
        return b,c,d,a
    else:
        return a,b,c,d        

def triagen(a=[],b=[],c=[]):
    """Generator to give random points within the triangle"""
    alpha,beta,gamma=generate_random()
    result_list=[alpha*i + beta*j + gamma*k for i,j,k in zip(a,b,c)]
    return result_list

def quadgen(a=[],b=[],c=[],d=[]):
    """Generator to give random points within the quad"""
    while True:
        if random.random()<0.5:
            yield triagen(b,d,a)
        else:
            yield triagen(b,d,c)

a,b,c,d=quadcheck([0,0,0], [1,0,0], [1,1,0],[0,1,0])
e,f,g,h=quadcheck([0,0,0], [0,1,0],[-1,-1,0],[-1,0,0])
a_quad = quadgen(a,b,c,d)
b_quad = quadgen(e,f,g,h)

print(f'A random point inside the quad A is {next(a_quad)}')
print(f'A random point inside the quad B is {next(b_quad)}')
