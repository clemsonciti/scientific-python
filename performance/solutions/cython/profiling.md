~~~
In [1]: from micro.counting import count_objects

In [2]: import numpy as np

In [3]: img = np.loadtxt('01.txt', delimiter=',', dtype=np.int32)

In [4]: count_objects(img)
Out[4]: 16

In [5]: %timeit count_objects(img)
351 µs ± 3.75 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


~~~
