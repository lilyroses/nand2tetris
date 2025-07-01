def is_valid_input(inpt):
  if isinstance(inpt, bool):
    return False

  if not isinstance(inpt, int):
    return False

  if (not inpt == 0) and (not inpt == 1):
    return False

  return True


