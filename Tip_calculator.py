print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip/100
total_tip = tip_as_percent * bill
Total_bill = total_tip + bill
bill_per_person = Total_bill / people
print(f"Each person should pay: {round(bill_per_person,2)}")