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
        return "Le moteur thermique démarre."

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @staticmethod
    def convert_miles_to_km(miles):
        return miles * 1.60934
    
if __name__ == "__main__":
    print(Car.convert_miles_to_km(100))
    print(Car.convert_miles_to_km(50))