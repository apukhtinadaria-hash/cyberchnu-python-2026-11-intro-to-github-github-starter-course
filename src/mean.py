def mean(number):
  # Type your code
  digits = str(number)
  total = 0
  for d in digits:
    total += int(d)
  return total/len(digits)

print(mean(42))
print(mean(12345))