import sys
import projetQ1 
import projetQ2 
from projetQ5 import *
import numpy as np
import time
import matplotlib.pyplot as plt


#global variable
random_matrix_values = np.random.randint(1, 10, size=(500, 500))
a=projetQ1.Matrix([500,500],random_matrix_values)
b=projetQ1.Matrix([500,500],random_matrix_values)
v=projetQ1.Matrix([500,1],random_matrix_values)

d=projetQ1.SparseMatrix([500,500],random_matrix_values,"yes")




aa=projetQ2.Matrix([500,500],random_matrix_values)
bb=projetQ2.Matrix([500,500],random_matrix_values)
vv=projetQ2.Matrix([500,1],random_matrix_values)

dd=projetQ2.SparseMatrix([500,500],random_matrix_values,"yes")

ee=projetQ2.SparseMatrix([500,500],random_matrix_values,"yes")

if  len(sys.argv) < 2:
    print("this is a message for the user, for you to test the correctness of the implemented functions there is a structure that you need to follow")
    print("Each function will be assimiliated to a number, you will therefore need to type the nymber of the function you want to test ")
    print("Another important aspect is some function have been written using some libraries and some didn't")
    print("therefore the structure to follow is interactive.py lib (if you want to test the function with a library) number (for a normal matrix)")
    print("or interactive.py noLib number  ")
    print("or interactive.py noLib number spars (for sparse matrix) ")
    print("The number one is for displaying a matrice")
    print("The number two is for the addition of two matrices")
    print("The number three is for the soustraction of two matrices")
    print("The number four is for the matrice vector multiplication ")
    print("The number five is for the matrice matrice multiplication")
    print("The number six is for the solving of a AX=b")
    print("The number seven the computing of the L1 norm")
    print("The number eight is for the computing of the L2 norm")
    print("The number nine is for the computing of the Linfinite norm")
    print('the ten is for the making of a binary matrix out of a randomly generated dense matrix')
    print('the eleven is for the computing of the U, S, Vt of a binary matrix after the use of the SVD method')
    print('the twelve is for the computing of the recommendations of movies based on randomly generated matrix, and given values such as liked movies and given movie index ')


    

    sys.exit()

elif  len(sys.argv) ==3 and   str(sys.argv[1])=="lib":

    number = str(sys.argv[2])

    if number == '1':#display
        a.display()
        sys.exit()
            
    elif number == '2':#add
        print(a.addition(b))
        sys.exit()
    elif number == '3':#sous
        print(a.soustraction(b))
        sys.exit()
    elif number == '4':
        print(a.matrix_vector_mult(v))
        sys.exit()
    elif number == '5':
        print(a.matrix_matrixmult(b))
        sys.exit()
    elif number == '6':
        print(a.solve(v))
        sys.exit()

elif  len(sys.argv) ==3 and   str(sys.argv[1])=="noLib":

    number = str(sys.argv[2])

    if number == '1':
        aa.display()
        sys.exit()
            
    elif number == '2':
        print(aa.addition(bb))
        sys.exit()
    elif number == '3':
        print(aa.soustraction(bb))
        sys.exit()
    elif number == '4':
        print(aa.matrix_vector_mult(vv))
        sys.exit()
    elif number == '5':
        print(aa.matrixMatrixmulti(bb))
        sys.exit()
    elif number == '7':
        print(aa.L1norm())
        sys.exit()
    elif number == '8':
        print(aa.forbeniusnorm())
        sys.exit()
    elif number == '9':
        print(aa.linfnorm())
        sys.exit()
    

    

            
elif  len(sys.argv) ==4 and str(sys.argv[3])=="spars" and str(sys.argv[1])=="lib":
    number = str(sys.argv[2])
    if number == '1' :
        d.display()
        sys.exit()
    if number == '6':
        print(d.solve(v))  
        sys.exit()
    


            
elif  len(sys.argv) ==4 and str(sys.argv[3])=="spars" and str(sys.argv[1])=="noLib":
    number = str(sys.argv[2])
    if number == '1' :
        dd.to_csr_with_row_info()

    elif number == '2':
        print(dd.addition(ee))
        sys.exit()
    
    elif number == '3':
        print(dd.soustraction(ee))
        sys.exit()

    elif number == '4':
        print(dd.soustraction(ee))
        sys.exit()
    
    elif number == '7':
        print(dd.L1norm())
        sys.exit()
    
    elif number == '8':
        print(dd.forbeniusnorm())
        sys.exit()

    elif number == '9':
        print(dd.linfnorm())
        sys.exit()

elif len(sys.argv) == 2 : 
    number = str(sys.argv[2])
    if number == "10": 
        data_processing()
        sys.exit()

    elif number == '11':
        DIMENSIONAL_REDUCTION()
        sys.exit()

elif len(sys.argv)==5:
    number = str(sys.argv[2])
    if number == '12':
        recommend(sys.argv[2], sys.argv[3], sys.argv[4])
        sys.exit()
   



    

    