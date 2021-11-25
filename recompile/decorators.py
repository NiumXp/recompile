from .utils import (
    isint
)

def swap(
    idx,
    idx_or_op,
    **options,
):
    if isint(idx_or_op):
        if idx == idx_or_op:
            raise ValueError()

    ...


def replace(
    idx_or_op_or_func,
    idx_or_op_or_seq=None,
    **options,
):
    if isint(idx_or_op_or_func) and isint(idx_or_op_or_seq):
        return swap(
            idx_or_op_or_func,
            idx_or_op_or_seq,
        )

    ...
