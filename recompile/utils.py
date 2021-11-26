from .types_ import *


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


iscall = callable


def _idxop(
    b: bytearray,
    i: IdxOrOp,
) -> OpCode:
    if iscall(i):       return i()
    if not isint(i):    return i
    if not _odd(i):     return b[i], b[i+1]
    raise ValueError("unexpected index")


def _idxopseq(
    b: bytearray,
    i: IdxOrOpOrSeq,
) -> Iterable[OpCode]:
    ...
