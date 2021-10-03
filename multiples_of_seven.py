# Ascript that return the multiples of 7 between 0 and given number.

def multiples_of_seven(num):
    for i in range(num):
        if i%2==0:
            print(i)
        else:
            continue
        
# test for range 200
multiples_of_seven(200)
