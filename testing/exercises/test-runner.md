
In this exercise, you will re-write your tests so that they can be
run using `py.test`. For example, the following test:

```python
from strflip import strflip

assert(strflip('') == '')
```

can be re-written as:

```python
def test_empty_string():
    assert(strflip('') == '')
``` 
