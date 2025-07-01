# NAND.py
from AND import AND
from NOT import NOT

def NAND(x, y):
  """NOT(x and y)."""
  a = AND(x,y)
  b = NOT(a)
  return b

