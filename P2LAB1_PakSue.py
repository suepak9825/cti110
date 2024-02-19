# Sue Pak
# 2/19/2024
# P2LAB1
# Write code that performs mathematical calculations and displays info to users

#Read in floating-point numbers from the user
gas_milage = float(input())
cost_of_gas = float(input())

#Calculate equivalent number of gas prices per miles
gas_20_miles = (cost_of_gas*20)/gas_milage
gas_75_miles = (cost_of_gas*75)/gas_milage
gas_500_miles = (cost_of_gas*500)/gas_milage

print(f'{gas_20_miles:.2f} {gas_75_miles:.2f} {gas_500_miles:.2f}')
