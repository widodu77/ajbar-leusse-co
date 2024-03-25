import sys
import projetQ1 
import projetQ2 
from projetQ5 import *
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.sparse import *
from scipy.sparse import random,csr_matrix




if  len(sys.argv) < 2:
    print("this is a message for the user, for you to test the correctness of the implemented functions there is a structure that you need to follow")
    print("Each function will be assimiliated to a number, you will therefore need to type the number of the function you want to test ")
    print("Another important aspect is some function have been written using some libraries and some didn't")
    print("therefore the structure to follow is interactive.py lib (if you want to test the function with a library) number (for a normal matrix)")
    print("or interactive.py noLib number  ")
    print("or interactive.py noLib number spars (for sparse matrix) ")
    print("the number one is for the addition of two matrices ")
    print("the number two is for the soustraction of two matrices ")
    print("the number three is for the computing of the L1 norm  ")
    print("the number four is for the computing of the L2 norm  ")
    print("the number five is for the computing of the Linfinite norm  ")
    print('the number six is for finding the differnet amount of time taken to compute the SVD method by scipy and numpy of the same randomly generated matrix, and the singular values of said matrices ')
    
    sys.exit()

elif len(sys.argv) ==3 and   str(sys.argv[1])=="lib" :

    number = str(sys.argv[2])

    if number=='1':

        size=[ 10,50,100,200,300,400,500,700,1000,2000,3000,5000]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ1.Matrix([i,i],a[0])
            f=projetQ1.Matrix([i,i],b[0])

            g=projetQ1.SparseMatrix([i,i],c[0],"yes")
            h=projetQ1.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.addition(f)
            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.addition(h)
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    

    elif number=='2':
        size=[ 10,50,100,200,300,400,500,700,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ1.Matrix([i,i],a[0])
            f=projetQ1.Matrix([i,i],b[0])

            g=projetQ1.SparseMatrix([i,i],c[0],"yes")
            h=projetQ1.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.soustraction(f)
            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.soustraction(h)
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    



elif len(sys.argv) ==3 and   str(sys.argv[1])=="noLib" :
    number = str(sys.argv[2])

    if number=='1':

        size=[ 5,10,20,40,80,160,320]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ2.Matrix([i,i],a[0])
            f=projetQ2.Matrix([i,i],b[0])

            g=projetQ2.SparseMatrix([i,i],c[0],"yes")
            h=projetQ2.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.addition(f)


            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.addition(h)
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    

    elif number=='2':
        size=[ 5,10,20,40,80,160,320]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ2.Matrix([i,i],a[0])
            f=projetQ2.Matrix([i,i],b[0])

            g=projetQ2.SparseMatrix([i,i],c[0],"yes")
            h=projetQ2.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.soustraction(f)
            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.soustraction(h)
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()

    elif number =='3':
        size=[ 5,10,20,40,80]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ2.Matrix([i,i],a[0])
            f=projetQ2.Matrix([i,i],b[0])

            g=projetQ2.SparseMatrix([i,i],c[0],"yes")
            h=projetQ2.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.L1norm()


            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.L1norm()
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='sparse')
        plt.plot(size, temps_sparse, label='dense')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    elif number =='4':
        size=[ 5,10,20,40,80,160,320,640]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ2.Matrix([i,i],a[0])
            f=projetQ2.Matrix([i,i],b[0])

            g=projetQ2.SparseMatrix([i,i],c[0],"yes")
            h=projetQ2.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.forbeniusnorm()


            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.forbeniusnorm()
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    
    elif number =='5':
        size=[ 5,10,20,40,80,160,320,640,1280]
        temps_dense=[]
        temps_sparse=[]

        for i in size:
            a=np.random.rand(1,i*i)
            b=np.random.rand(1,i*i)

            c = random(1, i*i, density=0.25, format="csr").toarray()
            d = random(1, i*i, density=0.25, format="csr").toarray()

            e=projetQ2.Matrix([i,i],a[0])
            f=projetQ2.Matrix([i,i],b[0])

            g=projetQ2.SparseMatrix([i,i],c[0],"yes")
            h=projetQ2.SparseMatrix([i,i],d[0],"yes")

            t1=time.time()
            e.linfnorm()


            t2=time.time()
            temps_dense.append(t2-t1)

            t3=time.time()
            g.linfnorm()
            t4=time.time()
            temps_sparse.append(t4-t3)
    
        plt.plot(size,temps_dense , label='dense')
        plt.plot(size, temps_sparse, label='sparse')
        plt.xlabel('Matrix Size')
        plt.ylabel('Time (s)')
        plt.xscale("log")
        plt.legend()
        plt.show()
    

elif len(sys.argv) ==2:
    number = str(sys.argv[2]) 
    if number == '6':
        np_vs_scipy_SVD()
        sys.exit()








