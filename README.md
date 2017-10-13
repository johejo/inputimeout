# inputimeout

## Description
Standard input with timeout.

## Install

```bash
$ pip install git+http://github.com/johejo/inputimeout.git
```

## Usage

```python
from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    print('Timeout!')
    something = 'something'
print(something)
```
## 
