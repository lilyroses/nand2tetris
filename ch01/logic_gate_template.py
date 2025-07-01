## !! CHANGE !! ##
# Xxx.py
from is_valid_input import is_valid_input


## !! CHANGE !! ##
def Xxx(inputs):
  if len(inputs) < 2:
    return -1

  for inpt in inputs:
    if not is_valid_input(inpt):
      return -1

  # do stuff
  pass


if __name__ == "__main__":
  from bits import xy_in, xyz_in
  from format_truth_table import format_truth_table as fmt

  ## !! CHANGE !! ##
  fn = "Xxx"

  inputs = xy_in
  ## !! CHANGE !! ##
  outputs = [Xxx(inpt) for inpt in inputs]
  table = fmt(inputs, outputs, fn)
  print(table)

  inputs = xyz_in
  ## !! CHANGE !! ##
  outputs = [Xxx(inpt) for inpt in inputs]
  table = fmt(inputs, outputs, fn)
  print(table)

