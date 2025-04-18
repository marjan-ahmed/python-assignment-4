def count_even(num_list: list[int]):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    
    if even_list:
        print("Even numbers:", even_list)
    else:
        print("No even number found")

def main():
    user_input = input("Enter integers (separated by commas): ")  # input stays as string
    num_list = [int(num.strip()) for num in user_input.split(",")]  # convert to list of ints
    count_even(num_list)

if __name__ == '__main__':
    main()
