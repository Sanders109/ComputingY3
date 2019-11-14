import numpy as np


def f(x): return np.exp(-x)*np.sin(x)


def Trzm(x0, xn, nmax, f):
    table = []
    for n in range(1,nmax):
        h = (xn-x0)/n
        x = np.linspace(x0, xn, n+1)
        s = 0
        sarray = f(x)
        out = sarray[::len(sarray)-1]
        array = sarray[1:-1]
        s0 = sum(out)
        s = sum(array)
        a = (h/2.0)*(s0+2*s)
        table.append([n,a])
    
    return(table)

    # 0.5*h*(y1+yn*2*(y2+....+yn-1))
print(Trzm(0, 2, 10, f))
#x = np.linspace(0, 1, 10)
#print(f(x))

def f_(x): return np.exp(-x)*(np.cos(x)-np.sin(x))#e^(-x) (cos(x) - sin(x))

def error(x0,xn,n,f_):
    x = np.linspace(x0, xn, n+1)
    maxf_ = max(f_(x))
    e = - (((xn-x0)**3)/(12*n))*abs(f_(x))
    return e

print(error(0,2,10,f_))