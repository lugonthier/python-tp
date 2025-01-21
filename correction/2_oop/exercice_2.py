import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Marque: {self.brand}, Modèle: {self.model}, Année: {self.year}"

    def age(self):
        return datetime.datetime.now().year - self.year


if __name__ == "__main__":
    car1 = Car("Opel", "Corsa", 2014)
    car2 = Car("Audi", "A1", 2020)

    print(car1.age())
    print(car2.age())