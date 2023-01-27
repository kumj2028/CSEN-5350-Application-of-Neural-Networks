"""Represent gas and electric cars."""

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")
    
    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")
    
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")
    
class ElectricCar(Car):
    """A simple model of an electric car."""
    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)
        # Attribute specific to electric cars.
        self.battery = Battery()
    
    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")
    
    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank!")

class Battery:
    """A battery for an electric car."""
    def __init__(self, size=75):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0
    def get_range(self):
        """Return the battery's range."""
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315