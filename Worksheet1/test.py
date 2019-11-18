import numpy as np

sarray = np.linspace(1, 10, 10, endpoint=True)
array = sarray[::len(sarray)-1]

print(sarray, array)