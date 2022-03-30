first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
action = input("Введите оператор: ")

if action == '+':
    print(int(first_number) + int(second_number))
elif action == '-':
    print(int(first_number) - int(second_number))
elif action == '*':
    print(int(first_number) * int(second_number))
elif action == '/':
    print(round((int(first_number) / int(second_number)), 2))
else:
    print("Try again")
