from numpy.lib.npyio import save
from scipy import io
import numpy as np
array=np.ones((4,4))
print(array)
np.savetxt('test.txt',array)
data = np.loadtxt('test.txt')
print(array)