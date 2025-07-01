# XOR.py
from x_AND_NOT_y import x_AND_NOT_y
from y_AND_NOT_x import y_AND_NOT_x

def XOR(x,y):
  a = x_AND_NOT_y(x,y)
  b = y_AND_NOT_x(x,y)
  c = OR(a,b)
  return c
