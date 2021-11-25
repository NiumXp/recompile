# recompile
A Python library to recompile code objects and other things with frame objects

## Install
...

## Quick examples
The `decorators` subpackage has a lot of useful decorators as examples of how to use the functions from the main package.

```python
from recompile.opcodes import *
from recompile.decorators import *


@replace(
    BIN_MUL,  # BINARY_MULTIPLY
    BIN_ADD,  # BINARY_ADD
)
def mul(x, y):
    """Returns the sum of `x` with `y`."""
    return x*y


assert mul(5, 2) == 7  # 7 = 5+2
assert mul(5, 1) == 5  # 6 = 5+1
```
