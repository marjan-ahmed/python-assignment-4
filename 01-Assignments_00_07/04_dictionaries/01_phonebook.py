user_info = {}  # ✅ Initialize dictionary once

def main():
    while True:
        user_name = input("Enter your name: ")
        phone_num = int(input("Enter your phone number: "))
        
        user_info[user_name] = phone_num  # ✅ Add to dictionary

        add_user = input("Do you want to add more users? (yes/no): ").lower()
        if add_user != 'yes':
            break

    # ✅ Print all stored users
    for key in user_info:
        print(f'User: {key}, Phone No: {user_info[key]}')

    print(user_info)
    
if __name__ == '__main__':
    main()