class Restaurant:
    """a simple attempt to represent a resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """initialize resturant name and cuisine"""
        self.name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """provide the resturant description"""
        print(f"{self.name.title()} serves wonderful {self.cuisine_type}!")

    def open_restaurant(self):
        """simulate opening the resturant"""
        print(f"{self.name.title()} is now open for business!")

    def set_number_served(self, number_served):
        """set number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """increment the number of customer that have been served"""
        self.number_served += additional_served


red_lobster = Restaurant('red lobster', 'seafood')

print(red_lobster.name.title())
print(red_lobster.cuisine_type.title())

red_lobster.set_number_served(12)
print(red_lobster.number_served)
red_lobster.increment_number_served(12)
print(red_lobster.number_served)

red_lobster.describe_restaurant()
red_lobster.open_restaurant()


# ludvigs = Restaurant("ludvig's bistro", 'seafood')
# ludvigs.describe_restaurant()

# mango_thai = Restaurant('mango thai', 'thai food')
# mango_thai.describe_restaurant()
