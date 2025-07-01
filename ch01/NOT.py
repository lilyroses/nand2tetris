# NOT.py
from is_valid_input import is_valid_input

def NOT(x):
  if not is_valid_input(x):
    return "ERROR"

  if x == 0:
    return 1
  return 0


if __name__ == "__main__":
  
