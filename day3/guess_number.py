from random import randint

print("Welcome to the Guess Number Game!")
print("I am thinking of a number between 1 and 100.")
secret_number = randint(1, 100)

print(type(secret_number))

for i in range(1,8):
    try:
        user_input = int(input("Guess Your Number: "))

        if user_input < 1 or user_input > 100:
            print("Please enter a number between 1 and 100.")
            continue
        elif user_input > secret_number:
            print("You guessed too high.")
        elif user_input < secret_number:
            print("You guessed too low.")
        else:
            print("You guessed correctly.")
            print(f"You have guessed the correct number {secret_number} in {i}th attempt.!")
            break

        if user_input != secret_number and i == 7:
            print("You have exhausted...No more chances left!!!")
    except ValueError:
        print("The character you have entered is not recognized, Please enter a number between 1 and 100.")

