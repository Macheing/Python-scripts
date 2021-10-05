'''
The guest_list function reads in a list of tuples with the name, age,
and profession of each party guest, and prints the sentence 
'''
def guest_list(guests):
    vowels = ['a','A','e','E','i','i','o','O','u','U']
    for (name,age,profession) in guests:
        if profession[0] == any(vowels):
            print('{} is {} years old and works as an {}.'.format(name,age,profession))
        else:
            print('{} is {} years old and works as a {}.'.format(name,age,profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
