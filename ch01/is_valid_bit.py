# is_valid_bit.py
def is_valid_bit(b):
  if type(b) != int:
    print(f"ERROR: {b} is non-int")
    return False

  if (b != 0) and (b != 1):
    print(f"ERROR: {b} is not a binary digit")
    return False

  return True


if __name__ == "__main__":
  from bits import xy_in, xyz_in
  for x, y in xy_in:
    print(x, y)
