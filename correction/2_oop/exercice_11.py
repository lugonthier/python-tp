from abc import ABC, abstractmethod
import datetime

class Vehicle(ABC):
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @abstractmethod
    def calculate_cost_per_km(self):
        pass

    @abstractmethod
    def get_max_range(self):
        pass

    def display_range(self):
        return f"Autonomie maximale: {self.get_max_range()} km"

class Car(Vehicle):
    total_cars = 0

    def __init__(self, brand, model, year, price, fuel_capacity, fuel_consumption, fuel_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0
        self.__price = price
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        Car.total_cars += 1

    def calculate_cost_per_km(self):
        consumption_per_km = self.fuel_consumption / 100
        return consumption_per_km * self.fuel_price

    def get_max_range(self):
        return (self.fuel_capacity / self.fuel_consumption) * 100


class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, price, battery_capacity, power_consumption, kwh_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
        self.battery_capacity = battery_capacity
        self.power_consumption = power_consumption
        self.kwh_price = kwh_price
        Car.total_cars += 1

    def calculate_cost_per_km(self):
        consumption_per_km = self.power_consumption / 100
        return consumption_per_km * self.kwh_price

    def get_max_range(self):
        return (self.battery_capacity / self.power_consumption) * 100

    def charge_time(self):
        return self.battery_capacity / 50
    
    
if __name__ == "__main__":
    thermal_car = Car(
        brand="Toyota",
        model="Corolla",
        year=2020,
        price=25000,
        fuel_capacity=50,
        fuel_consumption=6.5,
        fuel_price=1.8
    )

    electric_car = ElectricCar(
        brand="Tesla",
        model="Model 3",
        year=2022,
        price=45000,
        battery_capacity=75,
        power_consumption=16,
        kwh_price=0.15
    )

    vehicles = [thermal_car, electric_car]

    for vehicle in vehicles:
        print(f"\nType de véhicule: {vehicle.__class__.__name__}")
        print(f"Marque: {vehicle.brand}")
        print(f"Modèle: {vehicle.model}")
        print(f"Année: {vehicle.year}")
        print(f"Coût au kilomètre: {vehicle.calculate_cost_per_km():.2f}€")
        print(vehicle.display_range())
