import sys
import selectors
import platform

DEFAULT_TIMEOUT = 30.0
CRLF = '\r\n'
LF = '\n'


if platform.system() == 'Windows':
    LINE_FEED_CODE = CRLF
else:
    LINE_FEED_CODE = LF


class TimeoutOccurred(Exception):
    pass


def echo(string):
    sys.stdout.write(string)
    sys.stdout.flush()


def inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):

    echo(prompt)
    sel = selectors.DefaultSelector()
    sel.register(sys.stdin, selectors.EVENT_READ)
    events = sel.select(timeout)

    if events:
        key, _ = events.pop()
        return key.fileobj.readline().rstrip(LINE_FEED_CODE)

    else:
        echo(LINE_FEED_CODE)
        raise TimeoutOccurred
