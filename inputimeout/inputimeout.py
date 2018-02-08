import sys
import platform

if platform.system() == 'Windows':
    import msvcrt
    import time
else:
    import selectors
    import termios

DEFAULT_TIMEOUT = 30.0
INTERVAL = 0.05

SP = ' '
CR = '\r'
LF = '\n'
CRLF = CR + LF


class TimeoutOccurred(Exception):
    pass


def echo(string):
    sys.stdout.write(string)
    sys.stdout.flush()


def inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    if platform.system() == 'Windows':
        return win_inputimeout(prompt, timeout)
    else:
        return posix_inputimeout(prompt, timeout)


def posix_inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    echo(prompt)
    sel = selectors.DefaultSelector()
    sel.register(sys.stdin, selectors.EVENT_READ)
    events = sel.select(timeout)

    if events:
        key, _ = events[0]
        return key.fileobj.readline().rstrip(LF)
    else:
        echo(LF)
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
        raise TimeoutOccurred


def win_inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    echo(prompt)
    begin = time.monotonic()
    end = begin + timeout
    line = ''

    while time.monotonic() < end:
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            if c == CR or c == LF:
                echo(CRLF)
                return line
            if c == '\003':
                raise KeyboardInterrupt
            if c == '\b':
                line = line[:-1]
                echo(CR + prompt + line + SP)
            else:
                echo(c)
                line += c
        time.sleep(INTERVAL)

    echo(CRLF)
    raise TimeoutOccurred
