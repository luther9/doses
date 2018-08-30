#!/usr/bin/env python3

from os import environ
from sys import argv, exit, stderr


def main(argv, environ):
  try:
    print(float(argv[1]))
  except (IndexError, ValueError):
    print('doses takes one numerical argument', file=stderr)
    return 2
  home = environ.get('HOME', None)
  fileName = (home + '/' if home else '') + 'mydoses.scm'
  print(fileName)


if __name__ == '__main__':
  exit(main(argv, environ))
