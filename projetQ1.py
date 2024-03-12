import numpy as np
from scipy import linalg
from scipy.sparse import *

class Matrix:
    def __init__(self,size,values ):
        self.size=size
        self.values=values
    def matrix(self):
        a=np.array(self.values)
        b=a.reshape(self.size)
        return b

    def display(self):
        a=np.array(self.values)
        print(a.reshape(self.size ))
    
    def addition(self,m2):
        a=self.matrix()
        b=m2.matrix()

        return np.add(a,b)
    
    def soustraction(self,m2):
         a=self.matrix()
         b=m2.matrix()

         return np.subtract(a,b)
    
    def matrix_vector_mult(self,v1):
        a=self.matrix()
        b=v1.matrix()

        return np.dot(a,b)
    def matrix_matrixmult(self,m1):
        a=self.matrix()
        b=m1.matrix()

        return np.dot(a,b)


class DenseMatrix(Matrix):
    def __init__(self,size,values,sparcity ):
        Matrix.__init__(self,size,values)
        self.sparcity=sparcity in ["No","N","no","n"]
        
class SparseMatrix(Matrix):
    def __init__(self, size, values, sparcity):
        Matrix.__init__(self,size,values) 
        self.values = values  
        self.sparcity = sparcity in ["Yes", "Y", "yes", "y"]
    
    def matrix(self):
        data = self.values[0]
        indices = self.values[1]
        indptr = self.values[2]
        return csr_matrix((data, indices, indptr), shape=self.size)
    
    def display(self):
        a = self.matrix()
        return print(a)
    


a = SparseMatrix((3, 3), ([1, 2, 3], [0, 1, 2], [0, 1, 2, 3]), "yes")
b= SparseMatrix((3, 3), ([4, 5, 6], [0, 1, 2], [0, 1, 2, 3]), "yes")

print(a.addition(b))
print(a.matrix_matrixmult(b))
print(a.soustraction(b))

c=DenseMatrix((3,3),[[1,2,3],[4,5,6],[7,8,9]],"no")
d=DenseMatrix((3,3),[[9,2,3],[4,3,6],[7,6,9]],"no")
    
print(c.addition(d))
print(c.matrix_matrixmult(d))
print(c.soustraction(d))

e = SparseMatrix((3, 4), ([1, 2, 3, 4], [0, 1, 2, 3], [0, 1, 2, 4]), "yes")
g = SparseMatrix((3, 4), ([5, 6, 7, 8], [0, 1, 2, 3], [0, 1, 2, 4]), "yes")


h = SparseMatrix((4, 2), ([9, 8, 7, 6], [0, 1, 0, 1], [0, 1, 2, 3, 4]), "yes")


print(e.addition(g))
print(e.soustraction(g))
print(e.matrix_matrixmult(h))
