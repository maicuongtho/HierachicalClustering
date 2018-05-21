import math

def distance(a,b):
    x=float(a[0])-float(b[0])
    x=x*x
    y=float(a[1])-float(b[1])
    y=y*y
    dist=round(math.sqrt(x+y),2)
    return dist

def minimum(matrix):
    p=[0,0]
    mn=1000
    for i in range(0,len(matrix)):        
        for j in range(0,len(matrix[i])):            
            if (matrix[i][j]>0 and matrix[i][j]<mn):
                mn=matrix[i][j]
                p[0]=i
                p[1]=j
    return p 
            
def newpoint(pt):
    x=float(pt[0][0])+float(pt[1][0])
    x=x/2
    y=float(pt[0][1])+float(pt[1][1])
    y=y/2
    midpoint=[x,y]
    return midpoint

if __name__ == '__main__':    
    n=int(raw_input("Enter number of points.: "))
    points=list()
    outline='['
    i=0

    while(i<n):
        s=raw_input("Enter point (eg. 1,1)"+chr(65+i)+": ")
        c=s.split(",")
        points.append(c)
        i=i+1

    names={}

    for i in range(0,len(points)):
        names[str(points[i])]=chr(65+i)
    l=0
    while(len(points)>1):
        l=l+1
        matrix=list()
        print 'Distance matrix no. '+str(l)+': '
        for i in range(0,len(points)):
            m=[]
            for j in range(0,len(points)):
                m.append(0)
            for j in range(0,len(points)):
                m[j]=distance(points[i],points[j])
            print str(m)
            matrix.append(m)
        
        m=minimum(matrix)
        pts=list()
        p1=points[m[0]]
        pts.append(p1)
        points.remove(p1)
        p2=points[m[1]-1]
        pts.append(p2)
        points.remove(p2)   
        midpoint=newpoint(pts)
        points.append(midpoint)    
        c1=names.pop(str(p1))
        c2=names.pop(str(p2))
        names[str(midpoint)]="["+str(c1)+str(c2)+"]"    
        outline=names[str(midpoint)]
        
    print "Cluster is :",names[str(midpoint)]





