# NAND.py
from AND import AND
from NOT import NOT
from is_valid_input import is_valid_input


def NAND(*args):
  """NOT(AND)
  apply the AND function to all args, then perform the NOT operation.
  """
  if not is_valid_input(*args):
    return "ERROR"

  if len(args) < 2:
    return "ERROR"

  return  NOT(AND(args))


print(NAND(1,0,1))
