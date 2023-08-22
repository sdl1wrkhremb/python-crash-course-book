cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}

for city, stats in cities.items():
    print(f"{city}")
    country = stats['country']
    population = stats['population']
    mountains = stats['nearby mountains']
    print(f"\t{country}, {population}, {mountains}")
