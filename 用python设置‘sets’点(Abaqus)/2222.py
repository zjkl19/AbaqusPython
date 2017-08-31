from abaqus import *    
from abaqusConstants import *  
model='bb'
part='Part-2'
p = mdb.models[model].parts[part]
n = p.nodes
node=[]
for temp in range(len(n)):
    node0=temp,
    node1=n[temp].label,
    node2=node0+node1+n[temp].coordinates
    node+=[node2]
rnode=[]
for temp in range(len(n)):
    rnode0=temp,
    x=node[temp][2]
    y=node[temp][3]
    c=node[temp][4]
    if (x>0)&(y>=0):
        a=sqrt(x*x+y*y)
        b=atan(y/x)*180/pi    
    elif (x>0)&(y<0):
        a=sqrt(x*x+y*y)
        b=360+atan(y/x)*180/pi
    elif x<0:
        a=sqrt(x*x+y*y)
        b=180+atan(y/x)*180/pi
    elif x==0:
        a=sqrt(x*x+y*y)
        if y==0:
            b=0
        elif y>0:
            b=90
        elif y<0:
            b=270
    a1=a,
    b1=b,
    c1=c,
    rnode+=(rnode0+a1+b1+c1),
zuobiao=[]
for temp in range(len(rnode)):
    if (rnode[temp][1]>14)&(rnode[temp][2]>=59)&(rnode[temp][2]<=100):
        zuobiao+=rnode[temp][0],
nodes=n[zuobiao[0]:zuobiao[0]+1]
for xx in range(1,len(zuobiao)):
    x=zuobiao[xx]
    nodes+=n[x:x+1]
    
p.Set(nodes=nodes, name='Sets')


