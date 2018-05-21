import math
from operator import add

def inp():
    pts=raw_input('Enter Number of Points.: ')
    i=0
    global points
    points=[]
    b=[]
    while(i<int(pts)):
        a=raw_input('Enter point no.'+str(i+1)+': ')
        a=a.split(',')
        for pt in a:
            b.append(int(pt))    
        points.append(b)
        b=[]
        i=i+1
    k=int(raw_input("Enter value of k: "))
    kpoints=[]
    i=0
    while(i<int(k)):
        kpoints.append(points[i])
        i=i+1
    return kpoints
    
def dist(kpoints):
    distance=[]
    i=0
    while(i<len(kpoints)):
        c=kpoints[i]
        j=0
        g=[]
        while(j<len(points)):
            b=points[j]
            k=0
            l=0
            m=0
            while(k<len(b)):
                m=float(math.sqrt(math.pow((float(c[k])-float(b[k])),2)))
                l=float(l+m)
                k=k+1
            g.append(l)
            j=j+1
        distance.append(g)
        i=i+1
    return distance   

def bin_matrix(distance):        
    i=0
    dist1=''
    bm=[]
    G1=[]
    dist1=zip(*distance)
    while(i<len(dist1)):
        a=min(dist1[i])
        b=dist1[i].index(a)
        bm=[]
        j=0
        while(j<len(dist1[i])):
            if(j==b):
                bm.append(1)
            else:
                bm.append(0)
            j=j+1
        G1.append(bm)
        i=i+1
    return G1

def new_points(G):    
    b1=zip(*G)
    k=[]
    kpoints1=[]
    i=0
    while(i<len(b1)):
        j=0
        k=[]
        while(j<len(b1[i])):
            if(b1[i][j]==1):
                k.append(points[j])
            j=j+1
        kpoints1.append(k)
        i=i+1
    k1=[]
    newkpoints=[]
    for pt in kpoints1:
        if(len(pt)==1):
            newkpoints.append(pt[0])
        else:
            i=1
            a=[]
            b=[]
            g=[]
            a=(pt[0])
            while(i<(len(pt))):
                g=map(add,a,pt[i])
                b=(g)
                a=b
                i=i+1
            kp=[]
            for pt1 in a:
                kp.append(float(float(pt1)/float(len(pt))))
            newkpoints.append(kp)    
    return newkpoints

        
if __name__ == '__main__':
    kpoints=inp()
    distance=dist(kpoints)
    G1=bin_matrix(distance)
    newkpoints=new_points(G1)
    while 1:
        distance=[]
        distance=dist(newkpoints)
        G2=bin_matrix(distance)
        if(G1==G2):
            break
        else:
            G1=G2
            newkpoints=new_points(G1)
    
    b1=zip(*G1)
    k=[]
    kpoints1=[]
    i=0
    while(i<len(b1)):
        j=0
        k=[]
        while(j<len(b1[i])):
            if(b1[i][j]==1):
                k.append(points[j])
            j=j+1
        kpoints1.append(k)
        i=i+1
    print"__Clusters Are__:"    
    i=1
    for p in kpoints1:
        print 'Cluster '+str(i)+': ',p
        i=i+1
