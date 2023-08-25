class Restaurant:
    """a simple attempt to represent a resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """initialize resturant name and cuisine"""
        self.name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """provide the resturant description"""
        print(f"{self.name.title()} serves wonderful {self.cuisine_type}!")

    def open_restaurant(self):
        """simulate opening the resturant"""
        print(f"{self.name.title()} is now open for business!")
