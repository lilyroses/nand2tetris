# AND.py
from is_valid_input import is_valid_input


def AND(*args):
  if not is_valid_input(*args):
    return "ERROR"

  if len(args) < 2:
    return "ERROR"

  if 0 in args:
    return 0
  return 1


if __name__ == "__main__":
  from bits import xy_in, xyz_in
  from format_truth_table import format_truth_table as fmt

  fn = "AND"
  inputs = xy_in
  outputs = [AND(inpt) for inpt in inputs]

  table = fmt(inputs, outputs, fn)
  print(table)
