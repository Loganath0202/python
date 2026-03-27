
print("Welcome to the Pizza Order")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = str(input("Do you want pepperoni on your pizza? Y or N"))
extra_cheese = str(input("Do you want extra cheese? Y or N"))
total_bill = 0
if size == "S":
    total_bill = 15
elif size == "M":
    total_bill = 20
else:
    total_bill = 25

if pepperoni == 'Y':
    total_bill = total_bill + 2

if extra_cheese == 'Y':
    total_bill = total_bill + 3

print(f"Your total bill is {total_bill}")


