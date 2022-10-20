"""
Output:
weight = 85
height = 1.75
Your BMI is 28, you are slightly overweight.
"""

weight = float(input("Enter the weight : "))
height = float(input("Enter the height : "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    result =  "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "slightly overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"
print(f"Your BMI is {bmi}, you are {result}")