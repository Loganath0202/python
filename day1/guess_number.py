secret_number = 56

for i in range(0, 7):
    user_input = int(input("Enter your guess"))

    if secret_number == user_input:
        print("Congratulations!!!")
        break
    else:
        print("Not right!!! Guess a different number")