print("Give me two numbers, and I'll add them.")

try:
    first_number = int(input("\nFirst number: "))
    second_number = int(input("\nSecond number: "))
except ValueError:
    print("Please only enter numbers.")
else:
    print(first_number + second_number)
