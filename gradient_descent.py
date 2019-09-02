import matplotlib.pyplot as plt
import numpy as np
import math
np.set_printoptions(precision=2)

#Y=[]
#X=[]
Y=[1.1,1.5,2,3,5.5,6.5,6.8,7.9]
X=[1,2,3,4,5,6,7,8]
num=0



def generate_x_y(num):
    global X
    global Y
    rf=np.random.uniform(-5,5,10000)
    for i in range(num):
        X.append(i)
        Y.append(i+rf[i])


def gradient_descent(x,y,learn,itr,num):
    m=0
    b=0
    mse=0

    for i in range(itr):
        gm=((sum([(-1*x[j])*(y[j]-(m*x[j]+b)) for j  in  range(num) ]) * (2.0/num)))
        if math.isnan(gm) :
           print ("\nEXITED\n")
           exit(0) 
        gb=((sum([y[j]-(b+m*x[j]) for j in range(num)])*((-1)*2.0/num)))
        m=m -((learn)*gm)
        b=b -((learn)*gb)
        Yp=[ m*x[j]+b for j in range(num)]  
        mse=sum([(Y[j]-Yp[j])*(Y[j]-Yp[j]) for j in range(num)])/(1.0*num)
        print("m=%f b=%f mse=%f gm=%.10f gb=%.10f" %(m,b,mse,gm,gb))

    Yp=[]
    Xp=[]
    for i in range(10000):
        Xp.append(i)
        Yp.append(m*i+b)        
    plt.plot(Xp,Yp,color="green")
    plt.scatter(X,Y,color="blue")
    plt.show()

  
        
    


if __name__ == "__main__":
   learn=0.0000001
   itr=100000
   num=2000 
   generate_x_y(num)
   gradient_descent(X,Y,learn,itr,num)
