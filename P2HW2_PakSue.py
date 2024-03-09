#Sue Pak
#3/9/2024
#P2HW2
#Test ability to design a list

# Create an input for 6 modules
print(f'Enter grade for Module 1:', end = ' ')
module1 = float(input())

print(f'Enter grade for Module 2:', end = ' ')
module2 = float(input())

print(f'Enter grade for Module 3:', end = ' ')
module3 = float(input())

print(f'Enter grade for Module 4:', end = ' ')
module4 = float(input())

print(f'Enter grade for Module 5:', end = ' ')
module5 = float(input())

print(f'Enter grade for Module 6:', end = ' ')
module6 = float(input())

# Create a list to store all module inputs
module_grades_recorded = module1, module2, module3, module4, module5, module6

# Display different sequence-type functions of the recorded list
print()
print(f"{'Results':-^31}")
# Display the lowest number recorded by using the function min
print(f"{'Lowest Grade:':<17}{min(module_grades_recorded):>7}")

# Display the highest number recorded by using the function max
print(f"{'Highest Grade:':<17}{max(module_grades_recorded):>7}")

# Display the sum of the numbers recorded using function sum
print(f"{'Sum of Grades:':<17}{sum(module_grades_recorded)/len(module_grades_recorded):>7}")

# Display the average by dividing the sum by 6 and make it two decimal positions
print(f"{'Average:':<17}{(sum(module_grades_recorded))/6:>8.2f}")
print('----------------------------------------')

