import platform
import time

if platform.system() == 'Windows':
    import msvcrt
else:
    import sys
    import select

DEFAULT_TIMEOUT = 30.0


class TimeoutOccurred(Exception):
    pass


def inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    if platform.system() == 'Windows':
        return win_input_with_timeout(prompt=prompt, timeout=timeout)
    else:
        return unix_input_with_timeout(prompt=prompt, timeout=timeout)


def unix_input_with_timeout(prompt='', timeout=DEFAULT_TIMEOUT):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    (ready, _, _) = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n')
    else:
        raise TimeoutOccurred


def put_str(string):
    for c in string:
        msvcrt.putwch(c)


def win_input_with_timeout(prompt='', timeout=DEFAULT_TIMEOUT):
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
