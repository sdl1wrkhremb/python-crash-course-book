from car import Car
from battery import Battery


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


ryans_leaf = ElectricCar('nissan', 'leaf', '2023')
print(ryans_leaf.get_descriptive_name())

ryans_leaf.read_odometer()
ryans_leaf.increment_odometer(70000)
ryans_leaf.read_odometer()

ryans_leaf.battery.get_range()

ryans_leaf.battery.upgrade_battery()

ryans_leaf.battery.get_range()
