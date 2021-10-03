'''
The multiplication_table function prints the results of a number passed to it multiplied by 1 through 12.
An additional requirement is that the result is not to exceed 144
'''
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 12:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 144:
			#print('Result > 144')
			break
		print(str(number) + " x " + str(multiplier) + " = " + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24
