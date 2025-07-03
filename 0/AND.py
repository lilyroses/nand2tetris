# AND.py
def AND(x, y):
  if (x == 1) and (y == 1):
    return 1
  else:
    return 0


if __name__ == "__main__":
  x = int(input("x: "))
  y = int(input("y: "))
  ans = AND(x,y)
  print(f"AND({x},{y}) = {ans}")
