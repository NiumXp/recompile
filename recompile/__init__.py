__all__ = (
    "utils",
)

import typing as t
import utils


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
    code,
    idx_or_op,
    idx_or_op_or_seq,
    **options,
):
    carry = options.pop("ignore_arg", True) + 1

    if utils.iscode(code):
        code = code.co_code

    bs = code


def recompile(
    seq,
    **options,
):
    if not utils.isit(seq):
        seq = [*seq]

    ...


b = b"1234"
r = swap(b, 0, 2, arg=False)
print(r)
