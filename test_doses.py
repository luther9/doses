import doses


argv = ('', 0.5)
environ = {'HOME': '/home/somebodysusername'}


def test_noDataFile():
  """Return an error message when there's no mydoses.py file."""
  assert doses.main(argv, environ) == "Can't find mydoses.py in home directory."
