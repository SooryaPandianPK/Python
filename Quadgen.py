#Author:Soorya Pandian
import random
def generate_random():
    """Calling this function would return three different random numbers"""
    alpha=random.uniform(0,1)
    beta=random.uniform(0,1-alpha)
    gamma=1-alpha-beta
    return alpha,beta,gamma

def triagen(a=[],b=[],c=[]):
    """Generator to give random points within the triangle"""
    alpha,beta,gamma=generate_random()
    result_list=[alpha*i + beta*j + gamma*k for i,j,k in zip(a,b,c)]
    return result_list

def quadgen(a=[],b=[],c=[],d=[]):
    """Generator to give random points within the quad"""
    while True:
        if random.random()<0.5:
            yield triagen(a,b,c)
        else:
            yield triagen(a,c,d)
        
a_quad = quadgen([0,0,0], [1,0,0], [1,1,0],[0,1,0])
b_quad = quadgen([0,0,0], [0,1,0],[-1,-1,0],[-1,0,0])

print(f'A random point inside the quad A is {next(a_quad)}')
print(f'A random point inside the quad B is {next(b_quad)}')
