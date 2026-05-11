def squares_sum(n):
  # Type your code
  total = 0
  for i in range(1, n + 1):
    total += i ** 2
  return total


print(squares_sum(3))

