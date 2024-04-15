# Sue Pak
# 4/14/2024
# P4HW2
# Calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

employees = []
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

while True:
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    if employee_name.lower() == 'done':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (1.5 * pay_rate)
        overtime_total += hours_worked - 40
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    
    overtime_total += max(hours_worked - 40, 0)
    regular_pay_total += regular_pay
    gross_pay_total += regular_pay + overtime_pay
    num_employees += 1
    
    employees.append({
        'name': employee_name,
        'regular_pay': regular_pay,
        'overtime_pay': overtime_pay,
        'gross_pay': regular_pay + overtime_pay
    })

    print()
    print(f"Employee name:   {employee_name}")
    print()
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay     RegHour Pay      Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:.1f}           {pay_rate:.2f}      {max(hours_worked - 40, 0):.1f}         ${max(hours_worked - 40, 0) * 1.5 * pay_rate:.2f}           ${regular_pay:.2f}             ${regular_pay + overtime_pay:.2f}")
    print()
    print()

print()
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${overtime_total * 1.5 * pay_rate:.2f}")
print(f"Total amount paid for regular hours: ${regular_pay_total:.2f}")
print(f"Total amount paid in gross: ${gross_pay_total:.2f}")
