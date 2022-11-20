import random

def guess_range(x):
    random_number = random.randint(1,x-1)
    guess = 0
    lower_limit = 0
    upper_limit = x
    
    while guess != random_number:
        guess = int(input(f'Guess a number between {lower_limit} and {upper_limit}: '))
        if guess <= lower_limit or guess >= upper_limit:
            response = f'Guessed number is out of range! Guess again between {lower_limit} and {upper_limit}!'
            print(response)
            print(len(response) * '-')
            
        elif guess < random_number:
            lower_limit = guess
            response = f'You guessed too small! Guess again between {lower_limit} to {upper_limit}!'
            print(response)
            print(len(response) * '-')

        elif guess > random_number:
            upper_limit = guess
            response = f'You guessed too high! Guess again between {lower_limit} to {upper_limit}!'
            print(response)
            print(len(response) * '-')

    print(f'Boom~! You have guessed the number {random_number} !!')
    
  guess_range(10)
