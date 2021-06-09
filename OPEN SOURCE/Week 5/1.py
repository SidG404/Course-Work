import numpy as np
import matplotlib.pyplot as plt

def q1():
    pi = np.pi
    vals = np.array([-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi])
    sin,cos,tan, cot, sec, cosec = np.sin(vals),np.cos(vals),np.tan(vals), 1/np.tan(vals), 1/np.cos(vals), 1/np.sin(vals)
    
    plt.plot(vals, sin, label = 'Sin(x)')
    plt.legend()
    plt.show()

    plt.plot(vals, cos, label = 'Cos(x)')
    plt.legend()
    plt.show()
    
    plt.plot(vals, tan, label = 'Tan(x)')
    plt.legend()
    plt.show()

    plt.plot(vals, cot, label = 'Cot(x)')
    plt.legend()
    plt.show()

    plt.plot(vals, sec, label = 'Sec(x)')
    plt.legend()
    plt.show()

    plt.plot(vals, cosec, label = 'Cosec(x)')
    plt.legend()
    plt.show()
    


q1()