#import pytest

from doses import main

environ = {'HOME': '/home/somebodysusername'}


def test_noArgs():
  """Return 1 if the user doesn't give an argument."""
  assert main(('',), environ) == 1


def test_nonNumberArg():
  """Return 1 if the argument is not a number."""
  assert main(('', 'word'), environ) == 1


# Test for when there's no HOME.
