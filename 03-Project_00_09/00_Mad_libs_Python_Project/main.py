def main():
    print("\nFill In The Blanks")
    print("""
        Today I saw a ____ penguin at the ___.
        It was ____ with a balloon!
        """)
    fir_blank = input("Enter the adjective (1st blank): ")
    sec_blank = input("Enter the place (2nd blank): ")
    thr_blank = input("Enter the verb (3rd blank): ")
    print(f"\nToday I saw a {fir_blank} penguin at the {sec_blank}. It was {thr_blank} with a balloon!")
    

if __name__ == '__main__':
    main()