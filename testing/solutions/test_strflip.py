from strflip import strflip

assert(strflip('') == '')
assert(strflip('a') == 'a')
assert(strflip('ab') == 'ba')
assert(strflip('abab') == 'baba')
