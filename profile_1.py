import cProfile
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import solve
import projetQ1 
import projetQ2 

size1 = (150, 150)
values = np.random.rand(150, 150)
sparse_values = csr_matrix(values)

dense_matrix = projetQ1.Matrix(size1, values)
sparse_matrix = projetQ1.SparseMatrix(size1, values, "yes")

size2=(10,10)
values2 = np.random.rand(10, 10)
sparse_values2 = csr_matrix(values2)

dense_matrix2 = projetQ2.Matrix(size2, values2)
sparse_matrix2 = projetQ2.SparseMatrix(size2, values2, "yes")

vector1 = np.random.rand(150, 1)
vector2 = np.random.rand(10, 1)

def profile_matrix_operations1():
    print("display:")
    cProfile.run('dense_matrix.display()')
    print("addition:")
    cProfile.run('dense_matrix.addition(dense_matrix)')
    print("soustraction:")
    cProfile.run('dense_matrix.soustraction(dense_matrix)')
    print("matrixvectormult:")
    cProfile.run('dense_matrix.matrix_vector_mult(dense_matrix)')
    print("matrixmatrixmult:")
    cProfile.run('dense_matrix.matrix_matrixmult(dense_matrix)') 
    print("solve")
    cProfile.run('dense_matrix.solve(vector1)')
    print("display")
    cProfile.run('sparse_matrix.display()')
    print("solve")
    cProfile.run('sparse_matrix.ssolve(vector1)')


profile_matrix_operations1()

def profile_matrix_operations2():
    print("display:")
    cProfile.run('dense_matrix2.display()')
    print("addition:")
    cProfile.run('dense_matrix2.addition(dense_matrix2)')
    print("soustraction:")
    cProfile.run('dense_matrix2.soustraction(dense_matrix2)')
    print("matrxivectormult:")
    cProfile.run('dense_matrix2.matrix_vector_mult(vector2)')
    print("matrixMatrixmulti:")
    cProfile.run('dense_matrix2.matrixMatrixmulti(dense_matrix2)') 
    print("L1norm:")
    cProfile.run('dense_matrix2.L1norm()')
    print("L2norm:")
    cProfile.run('dense_matrix2.forbeniusnorm()')
    print("Linfinitenorm:")
    cProfile.run('dense_matrix2.linfnorm()')
    print("addition:")
    cProfile.run('sparse_matrix2.addition(sparse_matrix2)')
    print("soustraction:")
    cProfile.run('sparse_matrix2.soustraction(sparse_matrix2)')
    print("L1norm:")
    cProfile.run('sparse_matrix2.L1norm()')
    print("L2norm")
    cProfile.run('sparse_matrix2.forbeniusnorm()')
    print("Linfinitenom")
    cProfile.run('sparse_matrix2.linfnorm()')

profile_matrix_operations2()