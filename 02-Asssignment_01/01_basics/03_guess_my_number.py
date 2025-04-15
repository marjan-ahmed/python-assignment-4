# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def main():
    user_guessed = 0
    comp_guessed = random.randint(0, 99)

    while user_guessed != comp_guessed:
        user_guessed = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

        if user_guessed == comp_guessed:
            print(f"{comp_guessed} Congrats! The number was: {user_guessed}")
            
        elif user_guessed > comp_guessed:
            print("Your guess is too high")
        
        elif user_guessed < comp_guessed:
            print("Your guess is too low")
            
        else:
            print("Input valid guess")
    
if __name__ == '__main__':
    main()