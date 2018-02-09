import pytest

from inputimeout import inputimeout, TimeoutOccurred


class TestInputimeout(object):
    def test_inputimeout(self):
        with pytest.raises(TimeoutOccurred):
            inputimeout('>>', 3)
