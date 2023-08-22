favorites = {
    'ryan': ['5', '234234', '5876956785678'],
    'bob': ['13', '12', '11'],
    'frend': ['19', '21'],
    'john': ['3', '4', '5'],
    'ed': '4'
}

for name, numbers in favorites.items():
    print(f"{name.title()}\'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")
