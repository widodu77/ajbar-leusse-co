import projetQ1
import projetQ2
import random
import numpy as np
import time
import matplotlib.pyplot as plt


b=np.random.random_integers(9,size=(1,250000))
print(b)

c=np.random.random_integers(9,size=(1,250000))
print(b)
def matrix_moi_vs_scipy():

    size=[500,600,700,800,1000,1200,1500]
    temps_scipy=[]
    temps_moi=[]

    for i in size:
        b=np.random.random_integers(9,size=(1,i*i))
        c=np.random.random_integers(9,size=(1,i*i))
        a=projetQ1.Matrix((i,i),b[0])
        d=projetQ2.Matrix((i,i),c[0])
        t1=time.time()
        a.matrix()
        t2=time.time()
        temps_scipy.append(t2-t1)

        t3=time.time()
        d.matrix()
        t4=time.time()
        temps_moi.append(t4-t3)
    
    plt.plot(size,temps_scipy , label='Scipy')
    plt.plot(size, temps_moi, label='Moi')
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

def addition_moi_vs_scipy():

    size=[500,600,700,800,1000,1200,5000]
    temps_scipy=[]
    temps_moi=[]

    for i in size:
        b=np.random.random_integers(9,size=(1,i*i))

        e=np.random.random_integers(9,size=(1,i*i))

        f=np.random.random_integers(9,size=(1,i*i))
        
        c=np.random.random_integers(9,size=(1,i*i))
        
        a=projetQ1.Matrix((i,i),b[0])
        g=projetQ1.Matrix((i,i),e[0])
        


        d=projetQ2.Matrix((i,i),c[0])
        h=projetQ2.Matrix((i,i),f[0])

        t1=time.time()
        a.addition(g)
        t2=time.time()
        temps_scipy.append(t2-t1)

        t3=time.time()
        d.addition(h)
        t4=time.time()
        temps_moi.append(t4-t3)
    
    plt.plot(size,temps_scipy , label='Scipy')
    plt.plot(size, temps_moi, label='Moi')
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

def soustraction_moi_vs_scipy():

    size=[500,600,700,800,1000,1200,5000]
    temps_scipy=[]
    temps_moi=[]

    for i in size:
        b=np.random.random_integers(9,size=(1,i*i))

        e=np.random.random_integers(9,size=(1,i*i))

        f=np.random.random_integers(9,size=(1,i*i))
        
        c=np.random.random_integers(9,size=(1,i*i))
        
        a=projetQ1.Matrix((i,i),b[0])
        g=projetQ1.Matrix((i,i),e[0])
        


        d=projetQ2.Matrix((i,i),c[0])
        h=projetQ2.Matrix((i,i),f[0])

        t1=time.time()
        a.soustraction(g)
        t2=time.time()
        temps_scipy.append(t2-t1)

        t3=time.time()
        d.soustraction(h)
        t4=time.time()
        temps_moi.append(t4-t3)
    
    plt.plot(size,temps_scipy , label='Scipy')
    plt.plot(size, temps_moi, label='Moi')
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

def mult_moi_vs_scipy():

    size=[50,60,70,500]
    temps_scipy=[]
    temps_moi=[]

    for i in size:
        b=np.random.random_integers(9,size=(1,i*i))

        e=np.random.random_integers(9,size=(1,i*i))

        f=np.random.random_integers(9,size=(1,i*i))
        
        c=np.random.random_integers(9,size=(1,i*i))
        
        a=projetQ1.Matrix((i,i),b[0])
        g=projetQ1.Matrix((i,i),e[0])
        


        d=projetQ2.Matrix((i,i),c[0])
        h=projetQ2.Matrix((i,i),f[0])

        t1=time.time()
        a.matrix_matrixmult(g)
        t2=time.time()
        temps_scipy.append(t2-t1)

        t3=time.time()
        d.matrixMatrixmulti(h)
        t4=time.time()
        temps_moi.append(t4-t3)
    
    plt.plot(size,temps_scipy , label='Scipy')
    plt.plot(size, temps_moi, label='Moi')
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()



        
