# Sue Pak
# 3/15/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print()
print(f"{'Results':-^31}")
low = (min(grades))
print(f'{'Lowest Grade:':<17}{low:>7.1f}')
high = max(grades)
print(f'{'Highest Grade:':<17}{high:>7.1f}')
sum_grades = sum(grades)
print(f'{'Sum of Grades:':<17}{sum_grades:>8.1f}')
avg = sum_grades/len(grades)
print(f'{'Average:':<17}{avg:>8.2f}')
print('----------------------------------------')
# determine letter grade for average

if avg >= 90.00:
    print('Your grade is: A')
elif avg >= 80.00:
    print('Your grade is: B')
else:
    print('Your grade is: F') # TO DO: finish this






