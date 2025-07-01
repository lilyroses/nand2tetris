# x_AND_NOT_y.py
from AND import AND
from NOT import NOT

def x_AND_NOT_y(x,y):
  a = NOT(y)
  b = AND(x,a)
  return b

