
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
├── LICENSE.md
├── setup.py
```

2. Add the following to `setup.py`:

```
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

```{: .python}

3. Now, from the top level `micro` directory, install the package using `pip`:

```
$ pip install -e .
```

4. Try to import the micro package from Python:

```
In [1]: import micro

```

5. You should always also have a `README.md` and `LICENSE.md`:

* `LICENSE.md`: Explains if/how this software may be used by others. See for examples
<https://choosealicense.com/> or <https://opensource.guide/legal/>.

* `README.md`: Explains what this sofware does, how to install/use it, etc.,

6. Finally, upload to GitHub.

