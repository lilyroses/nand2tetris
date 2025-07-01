# AND.py
from is_valid_input import is_valid_input


def AND(x, y):
 
      return -1

  cond1 = (x == 1)
  cond2 = (y == 1)
  if (x == 1) and (y == 1):
    return 1


if __name__ == "__main__":
  from bits import xy_in, xyz_in
  from format_truth_table import format_truth_table as fmt

  fn = "AND"

  inputs = xy_in
  outputs = [AND(inpt) for inpt in inputs]
  table = fmt(inputs, outputs, fn)
  print(table)

  inputs = xyz_in
  outputs = [AND(inpt) for inpt in inputs]
  table = fmt(inputs, outputs, fn)
  print(table)
