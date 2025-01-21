import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

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

if __name__ == "__main__":
    car = Car("Ford", "Focus", 2020)
    print(f"Kilométrage initial: {car.get_odometer()} km")

    car.drive(150)
    print(f"Kilométrage après conduite: {car.get_odometer()} km")

    car.drive(-50)

    car.__odometer
