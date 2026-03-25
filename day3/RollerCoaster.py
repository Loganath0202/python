height = int(input("Enter your height in inches: "))
age = int(input("Enter your age: "))
photo = str(input("Take a photo: "))

fee = 0

if height > 120:
    print("You can ride roller coaster.")
    if age < 12:
        fee = 7
    elif age <= 18:
        fee = 12
    else:
        fee = 20
    if photo == "yes":
        fee = fee + 3
else:
    print("You can't ride coaster.")

print(f"your fee is {fee}")