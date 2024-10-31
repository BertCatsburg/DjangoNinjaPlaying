import pytest


def f():
    assert 2 + 2 == 5


def test_x():
    with pytest.raises(AssertionError):
        f()
