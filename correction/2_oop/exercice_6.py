import datetime

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0
        self.__price = price

    def display_info(self):
        return f"Marque: {self.brand}, Modèle: {self.model}, Année: {self.year}"

    def age(self):
        return datetime.datetime.now().year - self.year

    def get_odometer(self):
        return self.__odometer

    def drive(self, distance):
        if distance > 0:
            self.__odometer += distance
        else:
            print("Erreur : La distance doit être positive.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self.__price = value

    def start_engine(self):
        return "Le moteur thermique démarre."

class ElectricCar(Car):
    def __init__(self, brand, model, year, price, battery_capacity):
        super().__init__(brand, model, year, price)
        self.battery_capacity = battery_capacity

    def charge_time(self):
        return self.battery_capacity / 50

    def start_engine(self):
        return "Le moteur électrique démarre."