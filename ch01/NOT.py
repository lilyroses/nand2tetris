# OR.py
from is_valid_input import is_valid_input


def OR(x):
  if not is_valid_input(x):
    return "ERROR"

  if x == 0:
    return 1
  return 0

