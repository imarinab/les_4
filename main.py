first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
action = input("Enter operator: ")

if action == '+':
    print(f"Your result: {int(first_number)} + {int(second_number)} = {int(first_number) + int(second_number)}")
elif action == '-':
    print(f"Your result: {int(first_number)} - {int(second_number)} = {int(first_number) - int(second_number)}")
elif action == '*':
    print(f"Your result: {int(first_number)} * {int(second_number)} = {int(first_number) * int(second_number)}")
elif action == '/':
    print(f"Your result: {int(first_number)} / {int(second_number)} = {round((int(first_number) / int(second_number)), 2)}")
else:
    print("Try again")
