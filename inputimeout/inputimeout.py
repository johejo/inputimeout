import platform
import time

if platform.system() == 'Windows':
    import msvcrt
else:
    import sys
    import select


class TimeoutOccurred(Exception):
    pass


def inputimeout(prompt='', timeout=0.0):
    if platform.system() == 'Windows':
        return win_inputimeout(prompt=prompt, timeout=timeout)
    else:
        return unix_inputimeout(prompt=prompt, timeout=timeout)


def unix_inputimeout(prompt='', timeout=0.0):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    (ready, _, _) = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n')
    else:
        raise TimeoutOccurred


def win_inputimeout(prompt='', timeout=0.0):
    begin = time.monotonic()
    end = begin + timeout
    for c in prompt:
        msvcrt.putwch(c)
    line = ''
    time_up = True
    while time.monotonic() < end:
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            msvcrt.putwch(c)
            if c == '\r' or c == '\n':
                time_up = False
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
    if time_up:
        raise TimeoutOccurred
    return line
