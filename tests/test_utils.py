import inspect
from recompile import utils


def test_isint():
    assert utils.isint(5)
    assert not utils.isint(.5)
    assert not utils.isint('')


def test_iscode():
    f = inspect.currentframe()

    assert not utils.iscode(f)
    assert utils.iscode(f.f_code)


def test_isframe():
    f = inspect.currentframe()

    assert utils.isframe(f)
    assert not utils.isframe(f.f_code)


def test_isit():
    assert utils.isit([])
    assert not utils.isit(0)
