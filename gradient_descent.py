

Y=[1.1,1.5,2,3,5.5,6.5,6.8,7.9]
X=[1,2,3,4,5,6,7,8]


def gradient_descent(x,y,learn,itr):
    m=1
    b=1
    mse=0
    Yp=[];
    for i in range(itr):
        m=m -((learn)*((sum([(-1*x[j])*(y[j]-(m*x[j]+b)) for j  in  range(8) ]) * (2.0/8))))
        b=b -((learn)*((sum([y[j]-(b+m*x[j]) for j in range(8)])*((-1)*2/8.0))))  
        Yp=[ m*x[j]+b for j in range(8)] 
        mse=sum([(Y[j]-Yp[j])*(Y[j]-Yp[j]) for j in range(8)])/8.0
        print "m=%f b=%f mse=%f" %(m,b,mse)
        
    


if __name__ == "__main__":
   learn=0.00001
   itr=1000000
   gradient_descent(X,Y,learn,itr)
