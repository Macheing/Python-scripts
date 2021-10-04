def count_digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n):
		count += 1
		n = n//10
	return count
	
print(count_digits(25))   # Should print 2
print(count_digits(144))  # Should print 3
print(count_digits(1000)) # Should print 4
print(count_digits(0))    # Should print 1
