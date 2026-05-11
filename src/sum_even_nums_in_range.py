def sum_even_nums_in_range(start, stop):
  # Type your code
  total = 0
  for num in range(start, stop + 1):
    if num % 2 == 0:
      total += num
  return total

print(sum_even_nums_in_range(0, 10))
