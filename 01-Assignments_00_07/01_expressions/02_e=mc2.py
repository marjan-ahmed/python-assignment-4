# equation => e = mc²

# e = energy 
# m = mass
# c = speed of light

c = 299792458 

def main():
    mass = float(input("Enter the mass (kg): "))
    squared_c = c ** 2
    e = mass * squared_c
    print(f"E = {mass} * ({c})²")
    print(f"E = {mass} * {squared_c}")
    print(f"Energy is {e} J")    
    
    
if __name__ == '__main__':
    main()