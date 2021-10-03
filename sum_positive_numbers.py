# summation of positive number recursively.
def sum_positive_numbers(n):
    # check base case for and negative numbers.
    if n < 1:
        return 0
    else:
        # add all numbers between 1 and given number
        return n + sum_positive_numbers(n-1)
    
print(sum_positive_numbers(0)) # 0
print(sum_positive_numbers(1)) # 1
print(sum_positive_numbers(2)) # 3
print(sum_positive_numbers(6)) # 21
print(sum_positive_numbers(10)) # 55
