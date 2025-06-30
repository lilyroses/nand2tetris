# AND.py
from is_valid_input import is_valid_input


def OR(*args):
  if not is_valid_input(*args):
    return "ERROR"

  if len(args) < 2:
    return "ERROR"

  if 1 in args:
    return 1
  return 0


print(OR(10101, 100011))
