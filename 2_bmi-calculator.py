height = input("Insert your height: ")
weight = input("Insert your weight: ")

bmi = round(int(weight) / (int(height) / 100) ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, that means you are Underweight")
elif bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, that means you are Normal")
elif bmi >= 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, that means you are Overweight")
else:
    print(f"Your BMI is {bmi}, that means you are Obese")