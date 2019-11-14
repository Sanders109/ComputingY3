import numpy as np


def f(x): return np.exp(-x)*np.sin(x)


def Trzm(x0, xn, n, f):
    h = (xn-x0)/n
    x = np.linspace(x0, xn, n+1)
    s = 0
    sarray = f(x)
    out = sarray[::len(sarray)-1]
    array = sarray[1:-1]
    s0 = sum(out)
    s = sum(array)
    a = (h/2.0)*(s0+2*s)

    return(h, a)

    # 0.5*h*(y1+yn*2*(y2+....+yn-1))
print(Trzm(0, 2, 10, f))
x = np.linspace(0, 1, 10)
print(f(x))
