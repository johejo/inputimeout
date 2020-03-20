inputimeout
===========

[![image](https://img.shields.io/pypi/v/inputimeout.svg)](https://pypi.python.org/pypi/inputimeout)
[![image](https://img.shields.io/github/license/mashape/apistatus.svg)](https://raw.githubusercontent.com/johejo/inputimeout/master/LICENSE)
[![image](https://codecov.io/gh/johejo/inputimeout/branch/master/graph/badge.svg)](https://codecov.io/gh/johejo/inputimeout)

Description
-----------

Multi platform standard input with timeout

Install
-------

``` {.bash}
$ pip install inputimeout
```

Usage
-----

``` {.python}
from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    something = 'something'
print(something)
```

License
-------

MIT
