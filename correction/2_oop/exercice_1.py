class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Marque: {self.brand}, Modèle: {self.model}"
    
    
if __name__ == "__main__":
    car1 = Car("Opel", "Corsa")
    car2 = Car("Audi", "A1")

    print(car1.display_info())
    print(car2.display_info())