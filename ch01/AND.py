# AND.py
from is_valid_input import is_valid_input


def AND(*args):
  if not is_valid_input(*args):
    return "ERROR"

  if len(args) < 2:
    return "ERROR"

  if 0 in args:
    return 0
  return 1
