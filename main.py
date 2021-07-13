# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:21:52 2021

@author: JackC
"""

from math import tan,pi,atan,sin,asin
from matplotlib import pyplot as plt

class len:
    def __init__(self,r,f,tc,te,nd):
        self.r=r
        self.f=f
        self.tc=tc
        self.te=te
        self.nd=nd
        self.rr=((tc/2 - te/2)**2 + r**2)/(tc - te)
    def getYDWithYD(self,y,d):
        if(d==0):
            d=0.0000001
        #输入为y，与透镜中心面交点离光轴距离，d，入射角度(绝对角度)
        #输出为y，与透镜中心面交点离光轴距离，d，出射角度(绝对角度)
        k=-tan(d/180*pi)
        b=y
        tc=self.tc
        r=self.rr
        
        #print("d:"+str(d))
        #print("b:"+str(b))
        #print("k:"+str(k))
        #print("tc:"+str(tc))
        #print("rr:"+str(r))
        
        x=-(b - (2*b - k*(- 4*b**2 - 8*b*k*r + 4*b*k*tc + 4*k**2*r*tc - k**2*tc**2 + 4*r**2)**(1/2) + 2*k*r - k*tc)/(2*(k**2 + 1)))/k
        #y=(2*b + k*(- 4*b**2 - 8*b*k*r + 4*b*k*tc + 4*k**2*r*tc - k**2*tc**2 + 4*r**2)**(1/2) + 2*k*r - k*tc)/(2*(k**2 + 1))
        y=-k*x+b
        #得到左侧入射交点
        
        theta=atan((r-tc/2-x)/y)
        theta+=pi/2
        phi=d/180*pi
        
        theta=(theta+2*pi)%pi
        if(theta>pi/2):
            theta-=pi
        phi=(phi+2*pi)%pi
        if(phi>pi/2):
            phi-=pi
        
        #print("inang:"+str(inang/pi*180))
        print("phi:"+str(phi/pi*180))
        print("theta:"+str(theta/pi*180))
        print("x:"+str(x))
        print("y:"+str(y))
        
        
        inang=abs(phi-theta)
        ouang=asin(sin(inang)/self.nd)
        print("ina:"+str(inang/pi*180))
        print("oua:"+str(ouang/pi*180))
        
        if(phi<theta):
            out=theta-ouang
        else:
            out=theta+ouang
                
        out=(out+2*pi)%pi
        if(out>pi/2):
            out-=pi
        outy=y-tan(out)*x
        
        outo=out/pi*180
        print("out:"+str(outo))
        
        k=tan(out)
        b=outy
        x2=-(b - (2*b + k*(- 4*b**2 + 8*b*k*r - 4*b*k*tc + 4*k**2*r*tc - k**2*tc**2 + 4*r**2)**(1/2) - 2*k*r + k*tc)/(2*(k**2 + 1)))/k
        y2=-k*x2+b
        
        theta2=atan((x2-r+tc/2)/y2)
        theta2+=pi/2
        theta2=(theta2+2*pi)%pi
        if(theta2>pi/2):
            theta2-=pi
        print("theta2:"+str(theta2/pi*180))
        inang2=abs(out-theta2)
        ouang2=asin(sin(inang2)*self.nd)
        print("ina2:"+str(inang2/pi*180))
        print("oua2:"+str(ouang2/pi*180))
        
        print("x2:"+str(x2))
        print("y2:"+str(y2))
        if(out<theta2):
            out2=theta2-ouang2
        else:
            out2=theta2+ouang2
        outy2=y2-tan(out2)*x2
        out2=out2/pi*180
        print("out2:"+str(out2))
        print("outy2:"+str(outy2))
        
        print("")
        
        return outy,outo,x,outy2,out2,x2,y,y2
    
la=len(3,7.65,2.2,1,1.5168)

def drawroute(la,cnt,dcnt,rang,bgp,edp,dot=1):
    inlights=[]
    oulights=[]
    for i in range(-cnt//2,cnt//2+1):
        if(dot):
            inlights.append([i/(cnt/rang),atan(i/(cnt/rang)/bgp)/pi*180])
        else:
            inlights.append([i/(cnt/rang),0])
        oulights.append(la.getYDWithYD(inlights[-1][0],inlights[-1][1]))
    
    plt.grid()
    for l in range(cnt+1):
        x=[-bgp+(bgp+oulights[l][2])/100*i for i in range(dcnt)]
        y=[inlights[l][0]+tan(inlights[l][1]/180*pi)*i for i in x]
        plt.plot(x,y,c='green')
        
    for l in range(cnt+1):
        x=[edp*i/dcnt+oulights[l][5] for i in range(dcnt)]
        y=[oulights[l][3]+tan(oulights[l][4]/180*pi)*i for i in x]
        plt.plot(x,y,c='red')
    
    for l in range(cnt+1):
        x=[oulights[l][2],oulights[l][5]]
        y=[oulights[l][6],oulights[l][7]]
        print("x:")
        print(x)
        print("y:")
        print(y)
        plt.plot(x,y,c="blue")
    
    plt.show()

drawroute(la,30,100,4,10,10,0)
drawroute(la,30,100,4,10,10,1)
