import sys
import selectors
import platform

DEFAULT_TIMEOUT = 30.0
CRLF = '\r\n'
LF = '\n'

if platform.system() == 'Windows':
    import time
    import msvcrt
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

    if LINE_FEED_CODE == CRLF:
        return win_inputimeout(prompt, timeout)

    sel = selectors.DefaultSelector()
    sel.register(sys.stdin, selectors.EVENT_READ)
    events = sel.select(timeout)

    if events:
        key, _ = events.pop()
        return key.fileobj.readline().rstrip(LINE_FEED_CODE)

    else:
        echo(LINE_FEED_CODE)
        raise TimeoutOccurred


def put_str(string):
    for c in string:
        msvcrt.putwch(c)


def win_inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    begin = time.monotonic()
    end = begin + timeout
    put_str(prompt)
    line = ''

    while time.monotonic() < end:
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            if c == '\r' or c == '\n':
                put_str('\r\n')
                return line
            if c == '\003':
                raise KeyboardInterrupt
            if c == '\b':
                line = line[:-1]
                put_str('\r\n' + prompt + line)
            else:
                msvcrt.putwch(c)
                line = line + c
        time.sleep(0.05)
    raise TimeoutOccurred
