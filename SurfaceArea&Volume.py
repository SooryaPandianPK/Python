#Author : Soorya Pandian
def centroid(*arg):
    """Given a data structure of multidimesional dimensional points, this function returns the centroid"""
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
def FindArea(path):
    """Given a path of the stl file,this function returns the SurfaceArea and Volume"""
    with open(path,"r") as file:
        linelist = file.readlines()
        totallist=[]
        facelist=[]
        normal=[]
    for line in linelist:
        line=line.strip()
        lines=line.split()
        if line.startswith('facet'):
            normal=lines[2:]
            normal=[float(s) for s in normal]
            facelist.append(normal)
        elif line.startswith('vertex'):
            vertexlist=lines[1:]
            vertexlist=[float(s) for s in vertexlist]
            facelist.append(vertexlist)
        elif line.startswith('endloop'):
            totallist.append(facelist)
            facelist=[]
     
    import math
    vect1=[]
    vect2=[]
    cross=[]
    SurfaceArea=0
    Volume=0
    for face in totallist:
            midpoint=[]
            dA=0
            vect1=[b-a for a,b in zip(face[1],face[2])]
            vect2=[b-a for a,b in zip(face[1],face[3])]
            cross.append(vect1[1]*vect2[2]-vect1[2]*vect2[1])
            cross.append(vect1[2]*vect2[0]-vect1[0]*vect2[2])
            cross.append(vect1[0]*vect2[1]-vect1[1]*vect2[0])
            dA=0.5 * math.sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)
            SurfaceArea+=dA
            face[0]=[i*dA for i in face[0]]
            midpoint=centroid(face[1],face[2],face[3])
            for a,b in zip(face[0],midpoint):
                Volume+=a*b
            cross=[]
    Volume=Volume/3

    return SurfaceArea,Volume

path="D:/training/sphere1 3.stl"
SurfaceArea,Volume=FindArea(path)
print("The Surface area of stl file is :",SurfaceArea,"m^2")
print("The volume of the stl file is :",Volume,"m^3")





