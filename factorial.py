# return factorial number of given number
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
        print(result)
        
    return result

factorial(4) # should return 24
factorial(5) # should return 120
factorial(8) # should return 40320
factorial(12) # should return 479001600
