import sys

x, y, z = [int(c) for c in sys.argv[1:]]

def expression(x,y,z):
  result = int((x or y) and (not z))
  a = int(x or y)
  b = int(not z)
  c = int(a and b)
  print(f"{x} OR {y} = {a}")
  print(f"NOT {z} = {b}")
  print(f"{a} AND {b} = {c}")
#  print(f"({x} OR {y}) AND (NOT {z}) = {result}")

expression(x, y, z)


((not x) and y) and (not z)
