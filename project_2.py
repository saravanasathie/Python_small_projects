"""
Output:
Enter your current age : 21
You have 25185 days, 3588 weeks, and 828 months left.
"""
age = int(input("Enter your current age : "))
age = 90 - age          #Initially taking 90 as the last age to survive
days_remaining = age * 365
weeks_remaining = age * 52
months_remaining = age * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")