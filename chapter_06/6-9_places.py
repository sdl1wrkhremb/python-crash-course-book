favorite_places = {
    'john': ['mexico', 'canada', 'usa'],
    'susan': ['france', 'germany', 'italy'],
    'mary': ['africa', 'rome', 'california'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}\'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")
