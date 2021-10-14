print("Welcome to the Tip Calculator!")
print()
total_bill = input("What is the total bill? $")
tip = input("How much would you like to tip? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")

total_bill = (float(total_bill) * float(tip) /100) + float(total_bill)
per_person = (float(total_bill) / int(total_people))
format_total_tip = "{:.2f}".format(per_person)

print(f"The total for each person is ${format_total_tip}")

print()
print("Thank you for choosing our Tip Calculator!")
