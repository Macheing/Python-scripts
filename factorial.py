# return factorial number of given number
# using for loop 
def loop_factorial(num):
    result = 1
    for i in range(1,num+1):
        result = result*i  
    return result

# recursive factorial
def recursive_factorial(num):
    if num < 2:
        return 1
    return num * recursive_factorial(num-1)

print('For loop factorial vs Recursive factorial')
for num in range(100):
    print('Factorial of:',num, loop_factorial(num),'<== vs ==>',
              recursive_factorial(num))
    
    
    
