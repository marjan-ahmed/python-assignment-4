def main():
    dividend = int(input("Please enter a dividend: "))
    divisor = int(input("Please enter a divisor: "))
    remainder = dividend % divisor
    print(f"The remainder of {dividend}/{divisor} = {remainder}")

if __name__ == '__main__':
    main()