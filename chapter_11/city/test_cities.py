from city_functions import get_formatted_place


def test_city_country():
    """does a place like 'ocean city, new jersey' work"""
    formatted_place = get_formatted_place('ocean city', 'new jersey')
    assert formatted_place == 'Ocean City, New Jersey'


def test_city_country_population():
    """testing city country and population"""
    formatted_place = get_formatted_place('ocean city', 'new jersey', '500000')
    assert formatted_place == 'Ocean City, New Jersey - Population 500000'
