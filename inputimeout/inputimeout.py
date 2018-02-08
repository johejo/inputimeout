import sys
import platform
import time

if platform.system() == 'Windows':
    import msvcrt
else:
    import selectors

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


# def getch():
#     sel = selectors.DefaultSelector()
#     sel.register(sys.stdin, selectors.EVENT_READ)
#     events = sel.select(INTERVAL)
#
#     if events:
#         key, _ = events[0]
#         return key.fileobj.read(1)
#     else:
#         raise TimeoutOccurred
#
#
# def read_char():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch


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
