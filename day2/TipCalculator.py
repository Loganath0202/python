print("Welcome to the Tip Calculator")
bill = float(input("What is your total bill? "))
tip = int(input("How much percentage tip would you like to give? "))
persons = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = (total_bill/ persons)
print(round(bill_per_person,2))
