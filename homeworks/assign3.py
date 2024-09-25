import code 


class Vehicle():
    def __init__(self, make="Rivian", model="R1T", color="black", year=2024, speed=0):
        assert type(make) == str, "Make must be a string"
        assert type(model) == str, "Model must be a string"
        assert type(color) == str, "Color must be a string"
        assert type (year) == int, "Year must be an integer"
        assert type (speed) == int or type(speed) == float, "Speed must be a number"
        assert year > 0, "Year must be a positive integer"
        assert speed >= 0, "Speed must be 0 or greater"
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        assert amount > 0, "Acceleration must be positive"
        self.speed += amount

    def brake(self, amount):
        assert amount > 0, "Braking speed must be positive"
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return f"This car is a {self.year} {self.color} {self.make} {self.model} travelling at a speed of {self.speed} MPH."

    def __repr__(self):
        return f"Vehicle:'{self.make}','{self.model}','{self.color}',{self.year},{self.speed}"

class ElectricVehicle(Vehicle):
    def __init__(self, make="Rivian", model="R1T", color="black", year=2024, speed=0, battery_level=100.0):
        Vehicle.__init__(self, make, model, color, year, speed)
        assert type(battery_level) == int or type (battery_level) == float, "Battery level must be a number"
        assert 0 <= battery_level <= 100, "Battery level must be between 0 and 100"
        self.battery_level = battery_level

    def accelerate(self, amount):
        assert amount > 0, "Acceleration must be positive"
        if self.battery_level <= 0:
            raise AssertionError("Battery level is 0, cannot accelerate")
        self.speed += amount
        battery_decrease = (amount / 100) * 10
        self.battery_level -= battery_decrease
        if self.battery_level < 0:
            self.battery_level = 0

    def brake(self, amount):
        assert amount > 0, "Braking speed must be positive"
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        battery_increase = (amount / 100) * 5
        self.battery_level += battery_increase
        if self.battery_level > 100:
            self.battery_level = 100

    def __str__(self):
        return f"This electric car is a {self.year} {self.color} {self.make} {self.model} travelling at a speed of {self.speed} MPH with a battery level of {self.battery_level}%."

    def __repr__(self):
        return f"ElectricVehicle:'{self.make}','{self.model}','{self.color}',{self.year},{self.speed},battery:{self.battery_level}"
code.interact(local=dict(globals(), **locals()))