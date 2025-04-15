import random

def round_func(score):
    score = 0
    user = random.randint(1,100)
    computer = random.randint(1,100)
    print("Your number is", user)
    user_input = input("Do you think your number is higher or lower than the computer's? (h/l): ").lower()
    
    if user == computer:
        print("Congrats! you guessed it right")
        score+=2
        print("Your score is now", score)

    elif user_input == 'h' and user < computer:
        print(f"You were right! The computer's number was {user}")
        score+=2
        print("Your score is now", score)
        
    elif user_input == 'l' and user > computer:
        print(f"You were right! The computer's number was {user}")
        score+=2
        print("Your score is now", score)
        
    else:
        print("Aww, that's incorrect. The computer's number was", computer)
        score+=1
        print("Your score is now", score)
    

def main():
    print("""
    Welcome to the High-Low Game!
    -----------------------------
    """)
    round = 1
    while round != 6:
        print(f"Round {round}\n")
        round +=1
        round_func()
    

if __name__ == '__main__':
    main()