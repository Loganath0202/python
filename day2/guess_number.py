
print("Welcome to the Guess Number Game!")
print("I am thinking of a number between 1 and 100.")
secret_number = 98

for i in range(1,8):
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

