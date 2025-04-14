def main():
    fav_animal = input("Enter your favorite animal: ")
    print(f"My favorite animal is \x1B[1;3m{fav_animal}\x1B[0m") # using ANSI Escape Codes
    
if __name__ == '__main__':
    main()