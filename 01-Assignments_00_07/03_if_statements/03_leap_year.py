def main():
    year = int(input("Enter the year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year!")
    else:
        print("not a leap year")
    
if __name__ == '__main__':
    main()