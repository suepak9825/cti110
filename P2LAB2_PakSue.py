# Sue Pak
# 3/1/2024
# P2LAB2
# tests student's knowledge of how to write code that displays information to users

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product_nums = num1 * num2 * num3 * num4
avg_nums = (num1 + num2 + num3 + num4)/4

print(f'{product_nums:.0f}', end=' ')
print(f'{avg_nums:.0f}')

print(f'{product_nums:.3f}', end=' ')
print(f'{avg_nums:.3f}')
