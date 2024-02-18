# Sue Pak
# 2/18/2024
# P1HW2
# Using IDLE to create and test a program
print('This program calculates and displays travel expenses\n')
user_num = int(input('Enter Budget: '))
print()
user_location = input('Enter your travel destination: ')
print()
gas = int(input('How much do you think you will spend on gas? '))
print()
accomodation = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = int(input('Last, how much do you need for food? '))
print()
print('------------Travel Expenses------------')
print('Location:', user_location)
print('Initial Budget:', user_num)
print()
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
print()
sum_num = gas + accomodation + food
print('Remaining Balance:', user_num - sum_num)

# 1. Prompt the user to enter their budget
# 2. Store the budget entered by the user
# 3. Prompt the user to enter their travel destination
# 4. Store the travel destination entered by the user
# 5. Prompt the user to enter the amount they will spend on gas
# 6. Store the amount for gas entered by the user
# 7. Prompt the user to enter the amount they will spend on accommodation
# 8. Store the amount for accommodation entered by the user
# 9. Prompt the user to enter the amount they will spend on food
# 10. Store the amount for food entered by the user
# 11. Add the amounts entered for gas, accommodation, and food to get the total expenses
# 12. Subtract the total expenses from the budget
# 13. Display the budget remaining after subtracting expenses
