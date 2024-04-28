# Sue Pak
# 4/28/2024
# P5HW
#  Make the program a menu driven program. Meaning the program is to display a list of options to the user to choose from.

import random

def generate_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def add_numbers(num1, num2):
    total = num1 + num2
    return total

def subtract_numbers(num1, num2):
    total = num1 - num2
    return total

print("Welcome to Math Quiz")
print()

def menu():
    print("\nMAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

def main():
    while True:
        menu()
        choice = input("Please choose one of the menu options: ")

        if choice == "1":
            num1, num2 = generate_numbers()
            total = add_numbers(num1, num2)
            guesses = 0
            guess = int(input(f" {num1}\n+{num2}\n\nEnter answer.\n"))
            while guess != total:
                guesses += 1
                if guess < total:
                    guess = int(input("Sorry, guess is too low.\n\nTry again: "))
                else:
                    guess = int(input("Sorry, guess is too high.\n\nTry again: "))
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guesses + 1}")

        elif choice == "2":
            num1, num2 = generate_numbers()
            total = subtract_numbers(num1, num2)
            guesses = 0
            guess = int(input(f" {num1}\n-{num2}\n\nEnter answer.\n"))
            while guess != total:
                guesses += 1
                if guess < total:
                    guess = int(input("Sorry, guess is too low.\n\nTry again: "))
                else:
                    guess = int(input("Sorry, guess is too high.\n\nTry again: "))
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guesses + 1}")

        elif choice == "3":
            print("Thanks for playing...\nBye!!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
