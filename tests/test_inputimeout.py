import pytest

from inputimeout import inputimeout, TimeoutOccurred


def test_inputimeout():
    with pytest.raises(TimeoutOccurred):
        inputimeout(">>", 3)
