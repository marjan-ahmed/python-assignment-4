import random

def guess(user_num, comp_num):
    if comp_num > user_num:
        return "Oh! computer you got too far!\n"
    elif comp_num < user_num:
        return "Your guess is low!\n"
    elif comp_num == user_num:
        return "You guessed it right!🤖\n "
    else:
        return "Invalid Number"

def main():
    user_guess = 12  
    attempts = 0
    found = False

    while not found:
        comp = random.randint(1, 99)
        print(f"Computer's number: {comp} vs Guess: {user_guess}")
        result = guess(user_guess, comp)
        print(result)
        attempts += 1

        if comp == user_guess:
            found = True
            print(f"🎯 Match found in {attempts} attempts!")

if __name__ == '__main__':
    main()
