from typing import (
    Callable,
    Iterable,
    Any,
    Sequence,
    Union,
)
from types import (
    CodeType,
    FrameType,
)

Code = Union[bytes, bytearray, CodeType, FrameType]


def isint(obj: Any) -> bool:
    return isinstance(obj, int)


def iscode(obj: Any) -> bool:
    return isinstance(obj, CodeType)


def isframe(obj: Any) -> bool:
    return isinstance(obj, FrameType)


def isit(obj: Any) -> bool:
    return isinstance(obj, Iterable)


def bytearray_(obj: Code) -> bytearray:
    if isframe(obj): obj = obj.f_code
    if iscode(obj): obj = obj.co_code
    return bytearray(obj)


def _odd(x: int) -> bool:
    return bool(x%2)


def isodd(
    obj: Union[int, Sequence[int]],
    reduce: Callable[[bool], bool] = None,
) -> bool:
    if isint(obj): return _odd(obj)
    if reduce is None:
        reduce = all
    return reduce(map(_odd, obj))
