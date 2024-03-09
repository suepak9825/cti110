#Sue Pak
#3/9/2024
#P2LAB2
#Test ability to edit and enhance exiting programs

print('This program calculates and displays travel expenses')
print()
print('Enter Budget:', end = ' ')
budget = int(input())
print()
print('Enter your travel destination:', end = ' ')
travel_destination = input()
print()
print('How much do you think you will spend on gas?', end = ' ')
gas_estimate = int(input())
print()
print('Approximately, how much will you need for accomodation/hotel?', end = ' ')
accomodation_hotel_fees = int(input())
print()
print('Last, how much do you need for food?', end = ' ')
food_cost = int(input())
print()

print(f"{'Travel Expenses':-^39}")
print(f'Location:\t\t{travel_destination:}')
print(f'Initial Budget:\t\t${float(budget):.2f}')
print(f'Fuel:\t\t\t${float(gas_estimate):.2f}')
print(f'Accomodation:\t\t${float(accomodation_hotel_fees):.2f}')
print(f'Food:\t\t\t${float(food_cost):.2f}')
print('----------------------------------------')
print()
print(f'Remaining Balance:\t${float(budget-(gas_estimate+accomodation_hotel_fees+food_cost)):.2f}')
