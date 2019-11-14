import numpy as np

def f_(x): return np.exp(-x)*(np.cos(x)-np.sin(x))#e^(-x) (cos(x) - sin(x))

def maxerror(x0,xn,n,f_):
    x = np.linspace(x0, xn, n+1)
    maxf_ = max(f_(x))
    e = - (((xn-x0)**3)/(12*n))*abs(f_(x))
    return e

print(maxerror(0,2,10,f_))