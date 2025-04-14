def main():
    fahrenheit = int(input("Enter the temperature (F): "))
    c_calc = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {c_calc}°C") 

if __name__ == '__main__':
    main()