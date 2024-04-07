user_input = int(input())
user_input2 = int(input())

if user_input > user_input2:
    print("Second integer can't be less than the first.", end="")
else:
    for i in range(user_input, user_input2 + 1, 5):
        print(i, end = " ")
        
print()
