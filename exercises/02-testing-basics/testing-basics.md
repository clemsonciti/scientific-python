
In this exercise, you will write test cases for a function called
`strflip, which *flips* (reverses) a given string.
The function has already been written for you:

```python
def strflip(s):
    """
    strflip: Flip a string

    Parameters
    ----------

    s : str
        String to reverse

    Returns

    flipped : str
        Copy of `s` with characters in reverse order

    """
 
    flipped = ''

    # Starting from the last character in `s`,
    # add the character to `flipped`,
    # and proceed to the previous character in `s`.
    # Stop whenever we reach the first character.

    i = len(s)

    while True:
        
        i = i-1
        char = s[i]
        flipped = flipped + char

        # stop if we have reached the first character:
        
        if char == s[0]:
            break

    return flipped
```


Write and run a few tests for the above function. Some example tests are given below:

```python
assert(strflip('ab') == 'ba')
assert(strflip('mario') == 'oiram')
```

* Did any of your tests fail? How would you change the code to make those tests pass?

