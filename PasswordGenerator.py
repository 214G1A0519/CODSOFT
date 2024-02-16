import random
import string

def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive length for the password.")
            return

        password = generatePassword(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the password length.")

if __name__ == "__main__":
    main()
