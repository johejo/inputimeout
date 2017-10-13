# inputimeout

## Description
Standard input with timeout.

## Install

```bash
$ pip install inputimeout
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
