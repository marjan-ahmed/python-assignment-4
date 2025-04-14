inch = 12

def feet_to_inches(feet: int):
    calc = feet * inch
    print(f"{feet} foot = {calc} inches ")
    
def main():
    print("Foot to Inches Converter")
    input_feet = float(input("Enter the foots to: "))
    feet_to_inches(input_feet)
    
if __name__ == '__main__':
    main()