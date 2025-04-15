import random

game_choices = ['Rock', 'Paper', 'Scissor']

def game_mechanism(user, computer):
    if (user == 'rock' and computer == 'paper') or (user == 'scissor' and computer == 'rock') or (user == 'paper' and computer == 'scissor'):
        print("Oops! Computer wins 💻")
    
    elif (computer == 'rock' and user == 'paper') or (computer == 'scissor' and user == 'rock') or (computer == 'paper' and user == 'scissor'):
        print("You Win 🏆")  
    
    else:
        print("Match Tie!")

def main():
    user_action = input("Enter the action rock/paper/scissor): ").lower()
    print("You choose:", user_action) 
    comp_action = random.choice(game_choices).lower()
    print("Computer choose:", comp_action)
    game_mechanism(user_action, comp_action)
    
if __name__ == '__main__':
    main()