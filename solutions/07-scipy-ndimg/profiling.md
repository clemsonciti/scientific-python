```
In [1]: from micro.counting import count_objects

In [2]: import numpy as np

In [3]: img = np.loadtxt('01.txt', delimiter=',', dtype=np.int32)

In [4]: %timeit count_objects(img)
1.53 ms ± 53.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
