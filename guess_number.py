# import random library
import random

def guess(x):
    print()
    x = input('Enter a guess range of positive number: ')
    # check if x is number or else throw error.
    try:
            x = int(x)
    except:
            print('Invalid! please enter positive range number.')

    # secret number       
    random_num = random.randint(1,x)
    # user guess
    guess = 0
    count = 5
    while guess != random_num:
        print()
        guess = input(f'Guess a number between 1 and {x} or enter any character to exit the program: ')
        try:
            guess = int(guess)
        except:
            print()
            print('You just entered character:',guess,' to exit the program!')
            break
        

        # check remaining chance
        if count > 1:

            print('Count Down! you remain  with:', count,'chances.')

            if guess == random_num:
                print('Awesome! you won this time', guess, '=', random_num)

            elif guess > random_num:
                print('Incorrect!    Hint: your guess is bigger than secret number by:', (guess - random_num))

            else:
                print('Incorrect!   Hint: your guess is smaller than secret number by:',(guess-random_num))

        elif count == 1:
            print()
            print('Count Down! you remain  with:', count,'chance.')

            if guess == random_num:
                print('Awesome! you won this time', guess, '=', random_num)

            elif guess > random_num:
                print('Incorrect!   Hint: your guess is bigger than secret number by:', (guess - random_num))

            else:
                print('Incorrect!   Hint: your guess is smaller than secret number by:',(guess-random_num))


        else:
            print()
            print('Count Down! you remain  with:', count,'chance.')
            print('Sorry! you have used up all your chances of guessing.')
            print()
            break
        
        # count down
        count = count - 1




guess(1000)