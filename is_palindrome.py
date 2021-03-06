'''
The is_palindrome function checks if a string is a palindrome.
A palindrome is a string that can be equally read from left to right
or right to left,omitting blank spaces, and ignoring capitalization.
Examples of palindromes are words like kayak and radar,
and phrases like "Never Odd or Even"
'''
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	i = -1
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter != ' ' and input_string[i] != ' ':
			new_string += letter
			reverse_string += input_string[i]
		else :
			new_string += " "
			reverse_string +=' '
		i -= 1
	#print(new_string, 'vs',reverse_string)
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
