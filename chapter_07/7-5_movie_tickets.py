while True:
    age = input("Please enter your age:\n(Enter 'quit' when you are finished.)")
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You get in free!")
    elif age < 11:
        print("Your movie ticket will cost $10 please.")
    else:
        print("Your movie ticket will cost $15 please.")
