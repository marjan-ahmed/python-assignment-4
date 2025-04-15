from wonderwords import RandomWord

r = RandomWord()
random_word = r.word(include_parts_of_speech=["nouns", "adjectives"])

def main():
    word = random_word.lower()
    letters = list(word)
    display = ['_' for _ in word]
    guessed_letters = []
    max_attempts = 10
    attempts = 0  

    print("\n\tWelcome to Hangman!")
    print(" ".join(display))

    while '_' in display and attempts < max_attempts:
        user_guess = input("\nEnter a letter to save the hangman: ").lower()

        if user_guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(user_guess)
        attempts += 1

        if user_guess in letters:
            for i in range(len(letters)):
                if letters[i] == user_guess:
                    display[i] = user_guess
            print("✅ Good guess!")
        else:
            print("👎 Wrong guess!")

        print(" ".join(display))
        print(f"Attempts: {attempts}/{max_attempts}")

    if '_' not in display:
        print("🎉 Congratulations! You saved the hangman!")
    else:
        print("💀 Game Over! You've used all 10 attempts.")
        print(f"The word was: {word}")

if __name__ == '__main__':
    main()
