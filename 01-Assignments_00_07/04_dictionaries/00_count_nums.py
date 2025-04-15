def main():
    num_list = []
    num_count = {}  

    while True:
        num = input("Enter a number (or press Enter to stop): ")

        if num == "":
            break
        
        if num.isdigit():
            num = int(num)
            num_list.append(num)
              
            if num in num_count:
                num_count[num] += 1  
            else:
                num_count[num] = 1  
        else:
            print("Invalid input, please enter a valid number.")
    
    print("The list of numbers is:", num_list)
    
    print("Number count:", num_count)

if __name__ == '__main__':
    main()
