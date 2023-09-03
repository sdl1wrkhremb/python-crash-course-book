def get_formatted_place(city, country, population=''):
    """Generate a neatly formatted city and country."""
    if population:
        place = f"{city}, {country} - Population {population}"
    else:
        place = f"{city}, {country}"
    return place.title()
