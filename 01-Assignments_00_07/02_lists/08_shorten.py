max_length = 3

def shorten_list(lst: list):
    print("Your List:", lst)
    while len(lst) > max_length:
        lst.pop()
    print("Shorten List:", lst)

def main():
    shorten_list([1,3,5,7,9])
    
if __name__ == '__main__':
    main()