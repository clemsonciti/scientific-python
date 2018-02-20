
In this exercise you will time and profile
the function `count_objects` using
the IPython "magic" functions `%timeit`
and `%prun`.

1. Open the IPython interpreter or Jupyter Notebook.
1. Start by importing the `numpy` library and the `count_objects` function.
1. Navigate to the `scientific-computing/data` folder
1. Load the data from `01.txt` to a NumPy array `img`. Remember to
use `dtype=np.int32`.
1. Time and profile the statement `count_objects(img)`.

You can use the following magic command:

```python
In [1]: %timeit <python statement>
```

to obtain the running time for that Python statement.

Similarly, to obtain a profile, you can do:

```python
In [2]: %prun <python statement>
```
