# show_truth_tables.py
from AND import AND

from bits import xy_in, xyz_in
from is_valid_bit import is_valid_bit


def show_truth_table(fn, inputs, outputs, title=""):
  for inpt in inputs:
    if not is_valid_bit(inpt):
      print(f"ERROR: {inpt} invalid.")
      return

  if len(inputs) != len(outputs):
    print(f"ERROR: unmatched number of inputs/outputs.")
    return

  table = format_truth_table(fn, inputs, outputs)
  print(table)



if __name__ == "__main__":
  title = "x AND y (x*y)"
  fn = "AND"
  inputs = xy_in
  outputs = [AND(x,y) for x, y in inputs]
  show_truth_table(fn, inputs, outputs)
