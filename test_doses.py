#import pytest

from doses import main


argv = ('', 0.5)
environ = {'HOME': '/home/somebodysusername'}


def test_noArgs():
  """Return 2 if the user doesn't give an argument."""
  assert main(('',), environ) == 2


def test_nonNumberArg():
  """Return 2 if the argument is not a number."""
  assert main(('', 'word'), environ) == 2


def test_noHome():
  """Return None even if there's no HOME environment variable."""
  assert main(argv, {}) is None


def test_normal():
  """Return None in normal conditions."""
  assert main(argv, environ) is None
