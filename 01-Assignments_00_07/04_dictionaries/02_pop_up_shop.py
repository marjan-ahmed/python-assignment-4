def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    total = 0

    
    apple = int(input("How many (apple) do you want?: "))
    durian = int(input("How many (durian) do you want?: "))
    jackfruit = int(input("How many (jackfruit) do you want?: "))
    kiwi = int(input("How many (kiwi) do you want?: "))
    rambutan = int(input("How many (rambutan) do you want?: "))
    mango = int(input("How many (mango) do you want?: "))

    
    quantities = [apple, durian, jackfruit, kiwi, rambutan, mango]
    fruit_names = list(fruits.keys())
    
    for i in range(len(fruit_names)):
        fruit = fruit_names[i]
        quantity = quantities[i]
        price = fruits[fruit]
        total += quantity * price

    print(f"Your total is ${total}")

if __name__ == '__main__':
    main()
