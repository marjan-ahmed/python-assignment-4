def add_three_copies(list, message):
    for copies in range(3):
        list.append(message)
    
def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == '__main__':
    main()