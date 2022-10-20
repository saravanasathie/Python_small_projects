"""
Output:
Welcome to the tip calculator.
What was the total bill? $  => Input
What percentage tip would you like to give? 10, 12, or 15?  => Input
How many people to split the bill?  => Input
Each person should pay: $
"""

print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tips = (tip / 100) + 1
result = (total_bill / people) * 1
print("Each person should pay: ${:.2f}".format(result))
