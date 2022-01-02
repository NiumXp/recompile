import dis
from types import CodeType
from typing import Any


class CodeAssembler:
    __slots__ = (
        "_code",
        "names",
        "consts",
    )

    def __init__(self, code=None):
        # type: (CodeType | None) -> None
        self._code = code

        *self.names, = getattr(code, "co_names", ())
        *self.consts, = getattr(code, "co_consts", (None,))

    @property
    def instructions(self):
        """Return the instructions of the code object.
        """
        # type: () -> List[Instruction] | None

        if self._code:
            return dis.get_instructions(self._code)

    @property
    def raw(self):
        """Return the raw byte-code.
        """
        # type: () -> str

        ...

    def build(self):
        """Build the code object.
        """
        # type: () -> CodeType

        k = {}  # type: dict[str, Any]
        k["co_code"] = self.raw
        k["co_consts"] = self.consts

        code = CodeType(**k)

        return code
