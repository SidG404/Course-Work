import numpy as np
from scipy import linalg
import scipy
matrix1=np.array([[5,4],[6,3]])
a,b=scipy.linalg.eigvals(matrix1)
print("Eigen Values : ",a)
print("Eigen Vector : ",b)