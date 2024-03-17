# Sue Pak
# 3/16/2024
# P3LAB
# Display knowledge of how to write code that displays information to users

is_leap_year = False

input_year = int(input())

def is_leap_year(input_year):
    if input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0):
        return True
    else:
        return False

if is_leap_year(input_year):
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
