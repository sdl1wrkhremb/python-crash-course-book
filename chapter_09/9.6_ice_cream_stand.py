from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """represent aspects of a resturant specific to an ice cream resturant"""

    def __init__(self, resturant_name, cuisine_type='Ice Cream'):
        """
        initializes attributes of the parent class
        then initilie attributes specific to ice cream restaurants
        """
        super().__init__(resturant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """get the ice cream flavors"""
        print(f"{self.name} serves the following flavors: ")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


james_ice_cream_stand = IceCreamStand('Jame\'s Ice Cream Stand')
james_ice_cream_stand.flavors = ['Chocolate',
                                 'Cookies & Cream', 'Vanilla', 'Cookie Dough']

james_ice_cream_stand.display_flavors()
