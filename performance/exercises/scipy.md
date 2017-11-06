
In this exercise, you will re-implement the functions
`internal_match` and `external_match`
to use the `scipy.ndimage.binary_hit_or_miss` function.

0. Create a backup of the file `counting.py` called `counting.py.backup`
(you wouldn't have to do this if we were using Version Control).

1. In the original `counting.py`,
replace the code for the function `count_objects` with the following:

```
def count_objects(img):
    E = external_matches(img)
    I = internal_matches(img)
    return (E - I)/4
```

2. Implement the functions `external_matches` and `internal_matches`:

```
def external_matches(img):
    masks = [np.array([[0, 0], [0, 1]]),
             np.array([[0, 0], [1, 0]]),
             np.array([[1, 0], [0, 0]]),
             np.array([[0, 1], [0, 0]])]
    
    matches = 0
    for mask in masks:
        # ------ YOUR CODE HERE ------- #

        # ----------------------------- #
    return matches

def internal_matches(img):
    masks = [np.array([[1, 1], [1, 0]]),
             np.array([[1, 1], [0, 1]]),
             np.array([[0, 1], [1, 1]]),
             np.array([[1, 0], [1, 1]])]
 
    matches = 0 
    # ------ YOUR CODE HERE ------- #

    # ----------------------------- #
    return matches
```
3. Re-run the tests to make sure nothing is broken!
