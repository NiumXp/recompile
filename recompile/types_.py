from typing import *
from types import *

Code = Union[bytes, bytearray, CodeType, FrameType]
OpCode = Tuple[int, Union[int, str]]

ReturnsOpCode = Callable[..., OpCode]

IdxOrOp = Union[int, OpCode, ReturnsOpCode]
IdxOrOpOrSeq = Union[IdxOrOp, Iterable[IdxOrOp]]
