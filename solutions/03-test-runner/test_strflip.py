from strflip import strflip

def test_flip_empty():
    assert(strflip('') == '')

def test_flip_single():
    assert(strflip('a') == 'a')

def test_flip_two():
    assert(strflip('ab') == 'ba')

def test_flip_repeated():
    assert(strflip('abab') == 'baba')
