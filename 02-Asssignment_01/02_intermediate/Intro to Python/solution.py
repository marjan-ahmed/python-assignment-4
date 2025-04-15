planets_g = {
    'mercury': 37.6,
    'venus': 88.9,
    'mars': 37.8,
    'jupiter': 236.0,
    'saturn': 108.1,
    'uranus': 81.5,
    'neptune': 114.0,
}

earth_g = 9.8

def weight_calc(weight_on_earth):
    
    for planet, g in planets_g.items():
        gravity = round(g / 10, 2)
        print(planet.capitalize())

    planet_suggested = input("\nEnter a planet: ").lower()
    
    if planet_suggested in planets_g:
        gravity = planets_g[planet_suggested] / 10  # Convert to m/s²
        weight_on_planet = weight_on_earth * (gravity / earth_g)
        print(f"\nYour weight on {planet_suggested.capitalize()} would be {round(weight_on_planet, 2)} kg")
    else:
        print("Planet not found.")

def main():
    weight_on_earth = float(input("Enter your weight on Earth (kg): "))
    weight_calc(weight_on_earth)

if __name__ == '__main__':
    main()
