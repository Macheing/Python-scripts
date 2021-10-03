# sum of all squares within range of given number.
def sum_squares(x):
    sum = 0
    for i in range(x):
        sum += (i*i)
        #print(i,sum)
          
    return ('Total: ' + str(sum))

print(sum_squares(10))
