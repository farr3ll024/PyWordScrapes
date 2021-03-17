from itertools import *
from enchant.checker import SpellChecker

def main():
    letters = input("Enter letters: ")
    allowThreeLetter = input("Allow 3 letter words? (Y/N)")
    _perms = []
    _len = len(letters)
    _minLen = 4

    if allowThreeLetter == 'Y':
        _minLen = 3

    while(_len >= _minLen):
        _perms = _perms + [''.join(p) for p in permutations(letters, _len)]
        _len = _len - 1

    _perms = list(set(_perms))
    spell = SpellChecker()
    for p in _perms:
        if(spell.check(p)):
            print(p)

if __name__ == "__main__":
    main()


