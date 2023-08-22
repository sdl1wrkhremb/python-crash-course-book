rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"the {river} runs through {country}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
