sentence = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    new_sentence = sentence + " " + adjective + " " + noun + " " + verb + "!"
    print(new_sentence)   
    
if __name__ == '__main__':
    main()