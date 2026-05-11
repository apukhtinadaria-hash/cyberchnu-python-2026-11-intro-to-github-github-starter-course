def int_within_bounds(number, lower_bound, upper_bound):
  # Type your code
  if not isinstance(number, int):
    return False
  if number >= lower_bound and number < upper_bound:
    return True
  else:
    return False
print(int_within_bounds(6, -5, 5))

