# Sue Pak
# 3/24/2024
# P3HW2
# Create replica of program with correct formatting

# Ask user for employee details
employee = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Display employee name
print("-------------------------------------")
print(f'{"Employee name:":<6}{employee:>6}')
print()

# Calculate if branches on overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate amount employee should be paid for regular hours
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display all employee information
print('Hours Worked    Pay Rate    OverTime    OverTime Pay       RegHour Pay       Gross Pay')
print('-----------------------------------------------------------------------------------------------')
print(f'{hours_worked:<16.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<19.2f}${regular_pay:<18.2f}${gross_pay:.2f}')
