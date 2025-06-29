def is_valid_input(*args):
  for arg in args:
    if isinstance(arg, bool):
      return False
    if not isinstance(arg, int):
      return False
    if not (arg == 0 or arg == 1):
      return False
  return True


