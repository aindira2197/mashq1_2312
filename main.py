class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0  # Boshlang'ich tezlik 0

    def info(self):
        return f"Mashina: {self.brand} {self.model}, Tezlik: {self.speed} km/soat"

    def accelerate(self, km):
        self.speed += km
        print(f"Tezlik {km} ga oshdi.")

    def brake(self, km):
        if self.speed - km >= 0:
            self.speed -= km
        else:
            self.speed = 0
        print(f"Tezlik {km} ga kamaydi.")

# Foydalanish:
my_car = Car("Chevrolet", "Gentra")
my_car.accelerate(50)
print(my_car.info())
my_car.brake(20)
print(my_car.info())
