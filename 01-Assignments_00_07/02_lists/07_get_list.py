list = []

def main():
    message = input("Enter the value: ")
    while message:
        list.append(message)
        message = input("Enter the value: ")
    print(list)    

if __name__ == '__main__':
    main()