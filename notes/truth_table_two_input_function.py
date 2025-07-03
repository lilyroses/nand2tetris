# Truth table for a two input Boolean function

"""Function:
     - x = [0, 0, 1, 1]
     - y = [0, 1, 0, 1]

     XOR: (x and (not y)) or ((not x) and y)
     NOR: not(x or y)
     NAND: not(x and y)
"""

x = [0, 0, 1, 1]
y = [0, 1, 0, 1]


def constant_0(x, y):
  return [0 for i in x]

def constant_1(x, y):
  return [1 for i in x]


def is_x(x):
  return x

def is_y(y):
  return y



def AND(x, y):
  if not type(x) == list:
    return x and y
  return [int(x[i] and y[i]) for i in range(len(x))]


def NOT(x):
  if not type(x) == list:
    if x == 0:
      return 1
    return 0
  return [int(not n) for n in x]


def OR(x, y):
  if not type(x) is list and not type(y) is list:
    return x or y
  return [int(x[i] or y[i]) for i in range(len(x))]


def x_AND_NOT_y(x, y):
  return AND(x, NOT(y))

def NOT_x_AND_y(x, y):
  return AND(NOT(x), y)


def XOR(x, y):
  return OR(AND(x, NOT(y)), AND(NOT(x), y))

def NOR(x, y):
  return NOT(OR(x, y))


def equivalence(x, y):
  return OR(AND(x, y), AND(NOT(x), NOT(y)))


def if_y_then_x(x, y):
  return OR(x, NOT(y))

def if_x_then_y(x, y):
  return OR(NOT(x), y)

def NAND(x, y):
  return NOT(AND(x, y))


print(f"\nConstant 0:\n\tx = {x}\n\ty = {y}\n\tout = {constant_0(x, y)}")



print(f"\nAND:\n\tx = {x}\n\ty = {y}\n\tout = {AND(x, y)}")

print(f"\nx AND NOT y:\n\tx = {x}\n\ty = {y}\n\tout = {x_AND_NOT_y(x, y)}")

print(f"\nis x:\n\tx = {x}\n\tout = {is_x(x)}")

print(f"\nNOT x AND y:\n\tx = {x}\n\ty = {y}\n\tout = {NOT_x_AND_y(x, y)}")

print(f"\nis y:\n\ty = {y}\n\tout = {is_y(y)}")

print(f"\nXOR:\n\tx = {x}\n\ty = {y}\n\tout = {XOR(x, y)}")

print(f"\nOR:\n\tx = {x}\n\ty = {y}\n\tout = {OR(x, y)}")

print(f"\nNOR:\n\tx = {x}\n\ty = {y}\n\tout = {NOR(x, y)}")

print(f"\nEquivalence:\n\tx = {x}\n\ty = {y}\n\tout = {equivalence(x,y)}")

print(f"\nNOT y:\n\ty = {y}\n\tout = {NOT(y)}")

print(f"\nIF y THEN x:\n\tx = {x}\n\ty = {y}\n\tout = {if_y_then_x(x, y)}")

print(f"\nNOT x:\n\tx = {x}\n\tout = {NOT(x)}")

print(f"\nIF x THEN y:\n\tx = {x}\n\ty = {y}\n\tout = {if_x_then_y(x, y)}")

print(f"\nNAND:\n\tx = {x}\n\ty = {y}\n\tout = {NAND(x,y)}")

print(f"\nConstant 1:\n\tx = {x}\n\ty = {y}\n\tout = {constant_1(x, y)}")

x = 1
y = 1
print(f"XOR:\n\tx = {x}\n\ty = {y}\n\tout = {XOR(x,y)}")
