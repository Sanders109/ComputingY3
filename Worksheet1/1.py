import numpy as np
number = 0
array = []
while True:
    try:
        array.append(number)
        number += 1
    except MemoryError as error:
        # Output expected MemoryErrors.
        print(array[-1])
        break
