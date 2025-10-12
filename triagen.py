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
    while True:
        alpha,beta,gamma=generate_random()
        result_list=[alpha*i + beta*j + gamma*k for i,j,k in zip(a,b,c)]
        yield result_list
        
a_tria = triagen([0,0,0], [1,0,0], [1,1,0])
b_tria = triagen([0,0,0], [0,1,0], [-1,0,0])

print(f'A random point inside the triangle A is {next(a_tria)}')
print(f'A random point inside the triangle B is {next(b_tria)}')

