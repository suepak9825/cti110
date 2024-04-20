def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
        return 29
    else:
        return 28

if __name__ == '__main__':
    user_input = int(input())
    days_print = days_in_feb(user_input)

    print(f'{user_input} has {days_print} days in February.')
