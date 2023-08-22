person1 = {
    'first_name': 'bob',
    'last_name': 'smith',
    'age': '35',
    'city': 'small city'
}

person2 = {
    'first_name': 'fred',
    'last_name': 'evans',
    'age': '40',
    'city': 'big city'
}

people = [person1, person2]

# Display all of the information in the dictionary.

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    location = person['city']

    print(f"{name}, of {location}, is {age} years old.")
