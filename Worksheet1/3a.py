#import tkinter
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt

def f(x): return np.exp(-x)*np.sin(x)

x = np.linspace(0,np.pi)

plt.plot(x,f(x))
plt.title("Plot of e^(-x)sin(x)")
plt.show()

