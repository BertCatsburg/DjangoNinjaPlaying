import pytest

def f():
    raise SystemExit()


def test_error_test():
    with pytest.raises(SystemExit):  # This means, if there's an error in the code, that is good.
        # This should raise an error
        f()
