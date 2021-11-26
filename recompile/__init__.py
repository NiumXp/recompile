__all__ = (
    "utils",
)

import typing as t
from . import utils


def swap(
    code: utils.Code,
    x: int,
    y: int,
    **options,
) -> bytearray:
    assert x != y

    i = options.pop("arg", True) + 1

    b = utils.bytearray_(code)
    b[x:x+i], b[y:y+i] = b[y:y+i], b[x:x+i]

    return b


def replace(
    code: utils.Code,
    idx_or_op,
    idx_or_op_or_seq,
    **options,
):
    c = options.pop("count", None)

    b = utils.bytearray_(code)

    x, _ = utils._idxop(b, idx_or_op)
    y = utils._idxopseq(b, idx_or_op_or_seq)

    if not utils.isop(y):
        return b.replace(x, y, c)

    raise NotImplementedError()


def recompile(
    seq,
    **options,
):
    if not utils.isit(seq):
        seq = [*seq]

    ...
