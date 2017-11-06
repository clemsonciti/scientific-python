
~~~
In [1]: from micro.counting import count_objects

In [2]: import numpy as np

In [3]: img = np.loadtxt('01.txt', delimiter=',', dtype=np.int32)

In [4]: %timeit count_objects(img)
16.8 s ± 835 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [5]: %prun count_objects(img)
         15123506 function calls in 18.650 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2085382    4.144    0.000    4.144    0.000 {method 'reduce' of 'numpy.ufunc' objects}
  4174350    3.762    0.000    3.762    0.000 {built-in method numpy.core.multiarray.array}
   261121    2.814    0.000    9.016    0.000 counting.py:14(internal_match)
   261121    2.814    0.000    8.995    0.000 counting.py:3(external_match)
  2085382    1.839    0.000    8.979    0.000 fromnumeric.py:1973(all)
  2085382    1.092    0.000    5.760    0.000 {method 'all' of 'numpy.ndarray' objects}
  2085382    1.022    0.000    1.381    0.000 numeric.py:534(asanyarray)
        1    0.639    0.639   18.650   18.650 counting.py:25(count_objects)
  2085382    0.525    0.000    4.668    0.000 _methods.py:40(_all)
        1    0.000    0.000   18.650   18.650 {built-in method builtins.exec}
        1    0.000    0.000   18.650   18.650 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
~~~
