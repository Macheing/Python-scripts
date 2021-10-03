# return factorial number of given number
def factorial(n):
    result = 1
    for i in range(1,n):
        result = result*i  
        return result
    
# computing factorial consumes more memory like recursive functions
for n in range(0,10):
    print(n, factorial(n+1))
    
