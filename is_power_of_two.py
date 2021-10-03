# return true if number is to power of 2.
def is_power_of_two(num):
  # Check if the number can be divided by two without a remainder
  while num % 2 == 0 and num > 0:
    num = num / 2
  # If after dividing by two the number is 1, it's a power of two
  if num == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
