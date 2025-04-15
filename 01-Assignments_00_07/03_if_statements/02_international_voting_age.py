peturksbouipo_voting_age = 16
stanlau_voting_age = 25
mayengua_voting_age = 48
 
def main():
    user_age = int(input("How old are you? "))
    
    if user_age >= peturksbouipo_voting_age and user_age < stanlau_voting_age:
        print('You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.')
        
    elif user_age >= stanlau_voting_age and user_age < mayengua_voting_age:
        print("You can vote in Stanlau where the voting age is 25. You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Mayengua where the voting age is 48.")
        
    elif user_age >= mayengua_voting_age:
        print("You can vote in Mayengua where the voting age is 48. You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25.")
    
    else:
        print("Sorry! You cannot vote")

if __name__ == '__main__':
    main()