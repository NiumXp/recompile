__all__ = (
    "hook",
    "invoke",
)

from types import FunctionType
from typing import (
    Any,
    Dict,
    Callable,
)
from sys import version_info as version

try:
    from typing_extensions import TypeAlias
except (ImportError, ValueError):
    TypeAlias = Any

if version >= (3, 10, 0):
    from typing import TypeAlias  # type: ignore

HookHandler = Callable[..., Any]  # type: TypeAlias

_hooks = {}  # type: Dict[str, HookHandler | None]


def hook(
    name,  # type: str | HookHandler
    handler=None,  # type: HookHandler | None
):  # type: (...) -> HookHandler | None
    """Get or register a `HookHandler` for a hook name.
    """

    if isinstance(name, FunctionType):
        handler = name
        name = handler.__name__

    assert isinstance(name, str)

    return _hooks.setdefault(name, handler)


def invoke(
    name,  # type: str
    *args,  # type: Any
    **kwargs,  # type: Any
):  # type: (...) -> None
    """Invoke a `HookHandler` by name.
    """

    handler = _hooks.get(name)
    if handler:
        handler(*args, **kwargs)
