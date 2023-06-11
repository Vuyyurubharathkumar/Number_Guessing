import sys
import pdb
print("Guess a number in the range 1 to 10")

def guessing_number(start_number, end_number):
    while True:
        result = (start_number + end_number) // 2
        print(f"Is your number {result}?")
        user_input = input()
        if user_input.lower() == "yes":
            print("Voila! I guessed it right!!!")
            break
        elif user_input.lower() == "no":
            print(f"Is your number greater than {result}? (yes/no)")
            user_input = input()
            if user_input.lower() == "yes":
                start_number = result + 1
            elif user_input.lower() == "no":
                end_number = result - 1
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

guessing_number(1, 10)
