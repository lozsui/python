"""
Prompt for age. Ask when user wants to be retired. Then, print

You have X year left before you can retire.
It's CURRENT_YEAR, so you can retire in YEAR_RETIRED.
"""

from datetime import date

current_year = date.today().year
age = int(input("Enter your age: "))
retire_at = int(input("At what age do you want to retire? "))

years_left = retire_at - age
retire_year = current_year + years_left

print(f"You have {years_left} years left before you can retire.")
print(f"It's {current_year}, so you can retire in {retire_year}.")