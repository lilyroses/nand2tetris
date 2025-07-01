def is_valid_input(b):
  if isinstance(b, bool):
    return False

  if not isinstance(b, int):
    return False

  if (not b == 0) or (not b == 1):
    return False

  return True


