import cProfile
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import solve
import projetQ1 
# Assuming the Matrix and SparseMatrix classes are defined as you provided...

# Initialize some matrices for testing
size = (5, 5)
values = np.random.rand(5, 5)
sparse_values = csr_matrix(values)

dense_matrix = projetQ1.Matrix(size, values)
sparse_matrix = projetQ1.SparseMatrix(size, sparse_values, "yes")

# A vector for multiplication and solving
vector = np.random.rand(5, 1)

# Profile each method
def profile_matrix_operations():
    print("Profiling dense matrix operations:")
    cProfile.run('dense_matrix.display()')
    cProfile.run('dense_matrix.addition(dense_matrix)')
    cProfile.run('dense_matrix.soustraction(dense_matrix)')
    cProfile.run('dense_matrix.matrix_vector_mult(dense_matrix)')
    cProfile.run('dense_matrix.matrix_matrix_mult(dense_matrix)')
    cProfile.run('dense_matrix.solve(vector)')
    
    cProfile.run('sparse_matrix.display()')
    cProfile.run('sparse_matrix.ssolve(vector)')

profile_matrix_operations()
