## How to build

in the package root directory do the following

```
pipenv shell
python setup.py pytest
python setup.py bdist_wheel
```

then in the project that needs it

```
pip install /path/to/*.whl
```