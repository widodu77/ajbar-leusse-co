import projetQ1
import projetQ2
import random
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import linalg

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


# HERE IS THE LAMBDA FUNCTION - IT IS NOT USED AND IT IS ONLY HERE TO BE SHOWN
def modified_arr(arr):
    mod = list(map(lambda row: [1 if element > 2 else 0 for element in row], arr))
    return mod

# QUESTION 2,1 AND 2,2 -------------------------------------------------------------------------------------------------------------------

def data_processing(): 
    i = random.randint(55,150)
    j = random.randint(1,54)

    boke = np.random.randint(1, 10, size=(1,i*j)) # boke is "list" of the numbers that are going to be in the matrix as well as the size of said matrix 
    boken = projetQ1.Matrix((i,j),boke[0]) # boken is the size and values that are going to be in matrix baken
    #baken = boken.matrix() # baken is a matrix version of boken  

    bakugan = boken.to_binary() # bakugan is a binary matrix form of boken 

    #mod = list(map(lambda row: [1 if element > 2 else 0 for element in row], baken))
    print (bakugan)

    return bakugan



def testing_binary(): # THIS FUNCTION CHECKS IF THE BINARY PROCESSING THING WORKS BOTH FOR SQURe AND NON SQURE MATRICES, SPOIER ALERT< IT WORKS 
    i = 50
    j = 55
    square = data_processing(i,i)
    non_square = data_processing(i,j)
    return square, non_square

# QUESTIONS 2,3 -------------------------------------

def np_vs_scipy_SVD():

    size=[50,60,70,80,100,120,150]
    temps_scipy=[]
    temps_np=[]

    for i in size:
        b=np.random.random_integers(9,size=(1,i*i))
        c=np.random.random_integers(9,size=(1,i*i))

        a=projetQ1.Matrix((i,i),b[0])
        d=projetQ1.Matrix((i,i),c[0])

        t1=time.time()
        a.SVD_scipy()
        t2=time.time()
        temps_scipy.append(t2-t1)

        t3=time.time()
        U, S, Vt = d.SVD_np()
        t4=time.time()
        temps_np.append(t4-t3)
    
    plt.plot(size,temps_scipy , label='Scipy')
    plt.plot(size, temps_np, label='np')
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

    plt.plot([], [])  # Empty plot for setting labels and legends
    plt.scatter(range(len(S[:9])), S[:9], marker='o', label="Singular Values")  # Plotting only the singular values as points
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.legend()
    plt.yscale('log')  # Set y-axis to logarithmic scale

    plt.show()

    # AS YOU CAN SEE, NUMPY IS FASTER THEN SCIPY IN SVD DECOMP

    
# QUESTION 2,4-----------------------------------------------------------------------------------------------------------------------------------------

def pick_Singural_value(S):
    total = np.sum(S)
    cumulative_sum = 0 
    target = 0.9
    for i in range(len(S)):
        cumulative_sum += S[i]
        if (cumulative_sum/total) >  target: 
            return i + 1
    return len(S)


def DIMENSIONAL_REDUCTION(): 
    ahhh =  data_processing() #creation of the binary matrix 
    #getting the info of the matrix so that we can use it in the class "matrix"
    size = (len(ahhh), len(ahhh[0]))  # Size of the matrix
    values = [element for row in ahhh for element in row]  # Flatten the matrix

    euh = projetQ1.Matrix(size,values)  #adding the binary matrix into the class "matrix" so that we can use the functions in said class

    U, S, Vt = euh.SVD_np()

    num_singular_values = pick_Singural_value(S)  

    print( "U = ", U ,'S = ', S[:num_singular_values], 'Vt= ', Vt)

    return U , S[:num_singular_values], Vt  


DIMENSIONAL_REDUCTION()

# QUESTION 2,5 ----------------------------------------------------------------------------------------------------------------------------
def recommend(liked_movie_index, VT, selected_movies_num):
    recommended = []
    for i in range(VT.shape[0]):  # Iterate over rows of VT
        if i != liked_movie_index:
            # Calculate dot product of row i and liked movie index
            score = np.dot(VT[i], VT[liked_movie_index])
            recommended.append([i, score])
    
    # Sort recommended list based on the score
    final_rec = sorted(recommended, key=lambda x: x[1], reverse=True)
    
    # Select top selected_movies_num recommendations
    return final_rec[:selected_movies_num]

#print(recommend(1,Vt,2))






