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


def win_input_with_timeout(prompt='', timeout=DEFAULT_TIMEOUT):
    begin = time.monotonic()
    end = begin + timeout
    for c in prompt:
        msvcrt.putwch(c)
    line = ''
    is_timeout = True
    while time.monotonic() < end:
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            msvcrt.putwch(c)
            if c == '\r' or c == '\n':
                is_timeout = False
                break
            if c == '\003':
                raise KeyboardInterrupt
            if c == '\b':
                line = line[:-1]
            else:
                line = line + c
        time.sleep(0.05)
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    if is_timeout:
        raise TimeoutOccurred
    return line
