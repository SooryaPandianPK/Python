#Author : Soorya Pandian
def centroid(*arg):
    #Given a data structure of multidimesional dimensional points, this function returns the centroid
    count=len(arg)
    index=0
    dim=0
    centroid=[]
    for point in arg:
        if len(point)>dim:
            dim=len(point)
    for a in range(dim):
        element=0
        for point in arg:
            if len(point)-1 < index:
             continue
            element+=point[index]
        centroid.append(element/count)
        index+=1
    return centroid

print("The centroid of the given points is",centroid([1, 2, 3], [5, 6], [9, 7, 6, 5, 4], [21, 34], [75], [89], [-25, 90], [2, 3, 4] , [67], [1, 2, 3], [5, 6],[21, 34], [75], [89], [-25, 90], [2, 3, 4] ))
