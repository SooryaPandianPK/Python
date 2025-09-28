#Author : Soorya Pandian 
def FindArea(path):
    #Given a path of stl file, this function calculates the surface area
    with open(path,"r") as file:
        linelist = file.readlines()
        totallist=[]
        facelist=[]
        for line in linelist:
            line=line.strip()
            lines=line.split()
            if line.startswith('facet'):
                facelist.append(1)
            elif line.startswith('outer'):
                continue
            elif line.startswith('vertex'):
                vertexlist=lines[1:]
                vertexlist=[float(s) for s in vertexlist]
                facelist.append(vertexlist)
            elif line.startswith('endloop'):
                totallist.append(facelist)
            elif line.startswith('endfacet'):
                 facelist=[]
            elif line.startswith('endsolid'):
                break 

    import math
    vect1=[]
    vect2=[]
    cross=[]
    SurfaceArea=0
    for face in totallist:
        vect1=[a-b for a,b in zip(face[1],face[2])]
        vect2=[a-b for a,b in zip(face[1],face[3])]
        cross.append(vect1[1]*vect2[2]-vect1[2]*vect2[1])
        cross.append(vect1[2]*vect2[0]-vect1[0]*vect2[2])
        cross.append(vect1[0]*vect2[1]-vect1[1]*vect2[0])
        SurfaceArea+=0.5 * math.sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)
        cross=[]
    return SurfaceArea

print("The total surface area is ",FindArea("A:\personal\sphere1 3.stl"),"m^2")
