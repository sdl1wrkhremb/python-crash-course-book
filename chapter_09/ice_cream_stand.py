from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """attempt to represent an ice cream restaurant"""

    def __init__(self, resturant_name, cuisine_type):
        """initialize ice cream stand"""
        super().__init__(resturant_name, cuisine_type)
        self.flavors = []

    def get_flavors(self):
        """display the flavors of an ice cream restaurant"""
        if self.flavors:
            print(f"{self.name} serves the following flavors: ")
            for flavor in self.flavors:
                print(f"\t {flavor}")
        else:
            print(f"{self.name} doesn't have any flavors yet.")


ryans_stand = IceCreamStand('Ryans Ice Cream', 'Ice Cream')
ryans_stand.flavors = ['Chocolate', 'Vanilla',
                       'Cookies and Cream', 'Cookie Dough']
ryans_stand.get_flavors()

freds_stand = ryans_stand = IceCreamStand('Freds Ice Cream', 'Ice Cream')
freds_stand.get_flavors()
