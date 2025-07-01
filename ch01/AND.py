# AND.py
from is_valid_bit import is_valid_bit


def AND(x, y):
  if not is_valid_bit(x)w or not is_valid_bit(y):
    return

  if (x == 1) and (y == 1):
    return 1
  return 0


if __name__ == "__main__":
  from bits import xy_in
  for x, y in xy_in:
    print(f"AND({x}, {y}) = {AND(x,y)}\n")
  x = 1
  y = 3
  print(f"AND({x}, {y}) = {AND(x,y)}\n")

