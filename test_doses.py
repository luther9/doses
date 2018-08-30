from doses import main


argv = ('', 0.5)
environ = {'HOME': '/home/somebodysusername'}


def test_noArgs():
  """Return 2 if the user doesn't give an argument."""
  assert main(('',), environ) == 2


def test_nonNumberArg():
  """Return 2 if the argument is not a number."""
  assert main(('', 'word'), environ) == 2


def test_noDataFile():
  """Return an error message when there's no mydoses.py file."""
  assert main(argv, environ) == "Can't find mydoses.py in home directory."
