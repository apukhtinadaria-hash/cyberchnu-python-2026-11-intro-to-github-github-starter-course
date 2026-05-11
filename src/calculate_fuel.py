def calculate_fuel(distance):
  # Type your code
  fuel = distance * 10
  if fuel < 100:
    return 100
  return fuel


result = calculate_fuel(30)
print(result)
