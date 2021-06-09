from numpy.core.function_base import linspace
from numpy.matrixlib.defmatrix import matrix
from scipy import linalg
import numpy as np
import scipy
matrix1=np.array([[4,5],[3,2]])
a=scipy.linalg.det(matrix1)
print(a)
b=scipy.linalg.inv(matrix1)
print(b)
