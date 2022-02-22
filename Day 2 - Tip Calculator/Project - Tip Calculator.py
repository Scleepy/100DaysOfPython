print("Welcome to the tip calculator")

totalBill = float(input("What was the total bill? $"))

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

percentage = int(percentage)/100

people = int(input("How many people to split the bill? "))

tip_amount = totalBill * percentage

totalBill += tip_amount

print(f"Each person should pay: ${(totalBill/people):.2f}")
