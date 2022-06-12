import unittest

from inputimeout import inputimeout, TimeoutOccurred


class TestInputimeout(unittest.TestCase):
    def test_inputimeout(self):
        with self.assertRaises(TimeoutOccurred):
            inputimeout('>>', 3)
