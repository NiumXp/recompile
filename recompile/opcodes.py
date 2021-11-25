__all__ = []

from dis import opmap
from sys import version_info as version
from functools import wraps

_38 = (3, 8, 0)
_35 = (3, 5, 0)
_32 = (3, 2, 0)


def _(f):
    name = f.__name__

    __all__.append(name)

    @wraps(f)
    def function(*args):
        if not args:
            args = (0,)

        nonlocal name
        return opmap[name], args[0]

    return function


@_
def NOP():
    """
    NOP

    Do nothing code. Used as a placeholder by the bytecode optimizer.
    """
    ...


@_
def POP_TOP():
    """
    POP_TOP

    Removes the top-of-stack (TOS) item.
    """
    ...


@_
def ROT_TWO():
    """
    ROT_TWO

    Swaps the two top-most stack items.
    """
    ...


@_
def ROT_THREE():
    """
    ROT_THREE

    Lifts second and third stack item one position up, moves top down
    to position three.
    """
    ...


if version >= _38:
    @_
    def ROT_FOUR():
        """
        Lifts second, third and fourth stack items one position up,
        moves top down to position four.

        .. Added in version 3.8 of Python.
        """
        ...


if version >= _32:
    @_
    def DUP_TOP():
        """
        Duplicates the reference on top of the stack.
        """
        ...

    @_
    def DUP_TOP_TWO():
        """
        Duplicates the two references on top of the stack, leaving them
        in the same order.
        """
        ...


@_
def UNARY_POSITIVE():
    """
    Implements `TOS = +TOS`.
    """
    ...


@_
def UNARY_NEGATIVE():
    """
    Implements `TOS = -TOS`.
    """
    ...


@_
def UNARY_NOT():
    """
    Implements `TOS = not TOS`.
    """
    ...


@_
def UNARY_INVERT():
    """
    Implements `TOS = ~TOS`.
    """
    ...


@_
def GET_ITER():
    """
    Implements `TOS = iter(TOS)`.
    """
    ...


if version >= _35:
    @_
    def GET_YIELD_FROM_ITER():
        """
        If TOS is a generator iterator or coroutine object it is left
        as is. Otherwise, implements `TOS = iter(TOS)`.
        """
        ...
