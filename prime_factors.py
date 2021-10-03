def prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  print("factor " + ' number')
  # Keep going until the factor is larger than the number
  #print(factor,'<=>', number)
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      number = number / factor
      print(factor,'<=>',number)
      
    else:
      # If it's not, increment the factor by one
      factor +=1
      continue
      #print(factor)
      
  return "Done"

prime_factors(1000)# Should print 2,2,2,5,5,5
prime_factors(5000)# Should print 2,2,2,5,5,5,5
prime_factors(100)# Should print 2,2,5,5
