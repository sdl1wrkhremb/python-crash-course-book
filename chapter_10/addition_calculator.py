print("Give me two numbers, and I'll add them.")
print("Enter '00' to quit.")

while True:
    try:
        first_number = int(input("\nFirst number: "))
        if first_number == 00:
            break
        second_number = int(input("\nSecond number: "))
        if second_number == 00:
            break

    except ValueError:
        print("Please only enter numbers.")
    else:
        print(first_number + second_number)
