import random
import string

def main():
    print("Hello, Welcome to the password generator!")
    length = int(input("\nEnter the length of password: "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)

    print("The generated password is: " + password)

if __name__ == '__main__':
    main()