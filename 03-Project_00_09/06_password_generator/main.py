import random
import string  

small_alp = string.ascii_lowercase
capital_alp = string.ascii_uppercase
special_chr = '!@#$%^&*()[]`~'
numbers = range(70,99)

def password_generator(password, length):
    for i in range(password):
        mixed_chr_list = list(small_alp) + list(capital_alp) + list(str(special_chr)) 
        mixed_chr = random.sample(mixed_chr_list, length)
        mixed = "".join(mixed_chr)
        print(mixed)

def main():
    password = int(input("How many passwords do you need? "))
    length = int(input("What length should each password be? "))
    password_generator(password, length)
    
    
if __name__ == '__main__':
    main()