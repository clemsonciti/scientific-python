In this exercise, you will implement
a change to the *algorithm* used for
the functions `internal_match` and `external_match`
in our old version of `counting.py`.

Looking back at the previous version of `counting.py`,
we had the following implementations for the functions:

```python
def external_match(a):
    masks = [np.array([[0, 0], [0, 1]]),
             np.array([[0, 0], [1, 0]]),
             np.array([[1, 0], [0, 0]]),
             np.array([[0, 1], [0, 0]])]
    
    for mask in masks:
        if np.all(a == mask):
            return True
    return False

def internal_match(a):
    masks = [np.array([[0, 0], [0, 1]]),
             np.array([[0, 0], [1, 0]]),
             np.array([[1, 0], [0, 0]]),
             np.array([[0, 1], [0, 0]])]
    
    for mask in masks:
        if np.all(a == mask):
            return True
    return False
```

Rather than checking for the equivalence of
the subarray `a` with any of the masks,
it is more efficient to just compute the sum of the elements
of the subarray `a`,
and check if the sum is equal to `1` (for external matches),
or `3` for internal matches.

Replace the code that checks for equivalence (`np.all(a == mask)`)
with code that compares the sum to `1` or `3`.
The numpy function `np.sum` may be useful here.

* Make sure that all your tests still pass after making this change
* Time the code using `%timeit`, and compare with your previous values:
is the timing better than our initial implementation? Is it better
than using `scipy.ndimage.measurements.label`?
