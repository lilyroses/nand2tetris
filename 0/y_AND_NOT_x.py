# y_AND_NOT_x.py
from AND import AND
from NOT import NOT

def y_AND_NOT_x(x,y):
  a = NOT(x)
  b = AND(y,a)
  return b

