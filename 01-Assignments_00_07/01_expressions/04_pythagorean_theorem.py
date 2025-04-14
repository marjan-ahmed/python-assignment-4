# Pythagoras Theorem: 
# It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# BC ** 2 = AB ** 2 + AC ** 2

def main():
    side1 = float(input("Enter the lenght of AB: "))
    side2 = float(input("Enter the length of AC: "))
    pythagoras_calc = side1 ** 2 + side2 ** 2
    print("The length of BC (hypotenus) =", pythagoras_calc)
    
if __name__ == '__main__':
    main()