from inputimeout import inputimeout, TimeoutOccurred

if __name__ == '__main__':
    try:
        something = inputimeout(prompt='>>', timeout=5)
    except TimeoutOccurred:
        print('Timeout!')
        something = 'something'
    print(something)
