import numpy as np
from scipy import sparse
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
c=sparse.kron(matrix,matrix2).toarray()
print(c)
d=sparse.tril(matrix,k=-1)
print(d)
e=sparse.triu(matrix2,k=1)
print(e)