def chaotic_counting():
    for i in range(10):
        num = i + 1
        print(num)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()