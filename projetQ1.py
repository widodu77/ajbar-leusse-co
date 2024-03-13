import numpy as np
from scipy import linalg
from scipy.sparse import *
from scipy.sparse.linalg import spsolve

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
    
    def solve(self,b):
        a=self.matrix()
        return linalg.solve(a,b)


class DenseMatrix(Matrix):
    def __init__(self,size,values,sparcity ):
        Matrix.__init__(self,size,values)
        self.sparcity=sparcity in ["No","N","no","n"]
        
class SparseMatrix(Matrix):
    def __init__(self, size, values, sparcity):
        Matrix.__init__(self,size,values) 
        self.values = values  
        self.sparcity = sparcity in ["Yes", "Y", "yes", "y"]

    def matrix(arr):
        data = []  
        col_indices = []  
        row_indices = [0]  
    
        for i in arr:
            for col_index, value in enumerate(i):
                if value != 0:
                    data.append(value)
                    col_indices.append(col_index)
            row_indices.append(len(data)) 
    
        return data, col_indices, row_indices

    def solve(self,b):
        a=csr_matrix(self.values,shape=self.size)
        return spsolve(a,b)
    
    
    def display(self):
        a = self.matrix()
        return print(a)
    
    