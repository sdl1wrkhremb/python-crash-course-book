def describe_city(city, country='usa'):
    print(f"{city.title()} is in {country.title()}")


describe_city('new york')
describe_city('tokyo', 'japan')
describe_city(country='france', city='paris')
