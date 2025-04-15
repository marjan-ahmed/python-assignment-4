def tall_enough_extension(height: int):
    if height >= 50:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    height = int(input("\033[1;3mEnter your height: \033[0m"))
    while height:
        tall_enough_extension(height)
        height = int(input("\033[1;3mEnter your height: \033[0m"))

if __name__ == '__main__':
    main()