height = input("What is your height in inches: ")
weight = input("What is your weight in pounds: ")

bmi = (int(weight) / (float(height) ** 2) * 703)
print("Your BMI is:", int(bmi))