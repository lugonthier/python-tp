import datetime

class Car:

    total_cars = 0
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0
        self.__price = price

        Car.total_cars += 1

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
        return "Le moteur démarre."
    
class ElectricCar(Car):
    def __init__(self, brand, model, year, price, battery_capacity):
        super().__init__(brand, model, year, price)
        self.battery_capacity = battery_capacity

    def charge_time(self):
        return self.battery_capacity / 50

    def start_engine(self):
        return "Le moteur électrique démarre."
    
    
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020, 7000)
    car2 = Car("Opel", "Corsa", 2022, 12000)
    print(f"Total de voitures créées: {Car.total_cars}")

    car3 = ElectricCar("Tesla", "Model S", 2018, 40000, 200)

    print(f"Total de voitures créées: {Car.total_cars}")