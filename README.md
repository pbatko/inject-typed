# inject-typed

### Dependency Injection for Python driven by type annotations

Features:
- does not require changes to your code, for example no need to use special decorators
- fully driven by typed annotations from `__init__`



### Dev setup

```
dnf install python3.6
pip install virtualenv

virtualenv --python python36 inject-typed-env36

source inject-typed-env36/bin/activate

pip install -r requirements.txt
```


#### Pycharm
Mark `src` dir as `Source Root`


Resources:
https://virtualenv.pypa.io/en/latest/

### Releasing


python -m pip install --upgrade setuptools wheel
python -m pip install --upgrade twine

python setup.py sdist bdist_wheel




python -m twine upload --repository testpypi dist/*
python -m twine upload --repository pypi dist/*
username: __token__
pass: use API key



python -m pip install --index-url https://test.pypi.org/simple/ --no-deps inject-typed


python -m pip install --index-url https://test.pypi.org/simple/ --no-deps inject-typed

Resources:
https://packaging.python.org/tutorials/packaging-projects/
