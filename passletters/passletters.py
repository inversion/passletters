from __future__ import print_function
import getpass
import os
import sys

def main():
    password = getpass.getpass()

    SPACING = ' ' * 3
    print(SPACING.join(password))
    print(SPACING.join([str(i) for i in range(1, len(password) + 1)]))

    CLEAR_MSG = 'Press any key to clear the screen'
    if sys.version_info >= (3, 0):
        input(CLEAR_MSG)
    else:
        raw_input(CLEAR_MSG)

    # http://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
