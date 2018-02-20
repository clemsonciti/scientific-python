
In this exercise, you will re-write your tests so that they can be
run using `py.test`. For example, the following test:

```python
# file: test_strflip.py
from strflip import strflip

assert(strflip('') == '')
```

can be re-written as:

```python
def test_empty_string():
    assert(strflip('') == '')
```

After re-writing your tests as functions,
run the tests from the command-line using the
command:

```shellsession
$ pytest
```

* Did all your tests pass?
* What is the advantage of using a test runner like `pytest` over running tests manually?
