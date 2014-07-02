from __future__ import print_function
import getpass
import os
import sys
from colorama import init, Fore

def main():
    init()

    password = getpass.getpass()

    SPACING = ' ' * 3

    lines = [[] for i in xrange(3)]
    for number, letter in enumerate(password):
        numberStr = str(number)
        padding = ' ' * (len(numberStr) - 1)
        lines[0].append(Fore.GREEN + letter + Fore.RESET + padding)
        lines[1].append('^' + padding)
        lines[2].append(Fore.BLUE + numberStr + Fore.RESET)

    for line in lines:
        print(SPACING.join(line))

    CLEAR_MSG = 'Press any key to clear the screen'
    if sys.version_info >= (3, 0):
        input(CLEAR_MSG)
    else:
        raw_input(CLEAR_MSG)

    # http://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
