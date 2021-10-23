height = input("What is your height in inches: ")
weight = input("What is your weight in pounds: ")

bmi = (int(weight) / (float(height) ** 2) * 703)


if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}, You are underweight!")
elif bmi < 25:
    print(f"Your BMI is {round(bmi, 2)}, You have a normal weight!")
elif bmi < 30:
    print(f"Your BMI is {round(bmi, 2)}, You are slightly overweight!")
elif bmi < 35:
    print(f"Your BMI is {round(bmi, 2)}, You are obese!")
else:
    print(f"Your BMI is {round(bmi, 2)}, You are clinically obese. Time for a diet!")