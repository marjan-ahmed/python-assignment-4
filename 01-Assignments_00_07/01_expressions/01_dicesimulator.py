import random 

dice_sides = 6

def roll_dice():
    dice1 = random.randint(1, dice_sides)
    dice2 = random.randint(1, dice_sides)
    score = dice1 + dice2
    print("The score you get from 2 dices:", score)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))
    
    
if __name__ == '__main__':
    main()