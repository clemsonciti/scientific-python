
# Create your first package

In this exercise, you will create a package called `micro`
which can be installed with `pip`,
and then imported from anywhere on your computer.

We will develop this package to contain tools to analyze
the microscopy data that we plotted during the warmup exercise.

1. Create the following files and directories:

```
micro/
├── micro/
│   ├── __init__.py
├── README.md
├── LICENSE.txt
├── setup.py
```

2. Add the following to `setup.py`:

```python
from setuptools import setup

setup(name='example',
    version='0.1',
    description='The ultimate example',
    url='http://github.com/author/example',
    author='Author Name',
    author_email='author@example.com',
    license='MIT',
    packages=['example'],
    zip_safe=False)
```

3. Now, from the top level `micro` directory, install the package using `pip`:

```
$ pip install -e .
```

4. Try to import the micro package from Python:

```
In [1]: import micro

```

5. You should always have a `README.md` that contains (at the very least):

* The name and objectives of the project
* How to install the project
* If you want contributions or not

6. In addition, you should always have a `LICENSE.txt`
that explains if/how this software may be used by others.
Many open-source licenses are available to choose from:
<https://choosealicense.com/licenses/>. Working in pairs, choose a license
that you think would be appropriate for this work.

7. Finally, upload your project to GitHub.
