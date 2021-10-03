'''
 The sum of all the divisors of a number, without including it.
 A divisor is a number that divides into another without a remainder.
'''

def sum_divisors(num):
  sum = 0
  # Return the sum of all divisors of n, not including n
  divisor = 1
  while divisor < num:
      if num % divisor == 0:
        sum += divisor
        divisor += 1
      else:
        divisor += 1

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
print(sum_divisors(150)) # 222
print(sum_divisors(200)) # 265
