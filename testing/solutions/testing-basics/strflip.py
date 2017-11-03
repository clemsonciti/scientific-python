
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
 
    if len(s) == 0:
        return ''

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
        
        if i == 0:
            break

    return flipped


# alternate, clever solution:
def strflip2(s):
    return s[::-1]
