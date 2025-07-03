# NOR.py
from NOT import NOT
from OR import OR

def NOR(x,y):
  """NOT(x OR y)"""
  a = OR(x,y)
  b = NOT(a)
  return a
