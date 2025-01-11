class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return f'{self.make} {self.model}'
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def get_info(self):
        return f'{super().get_info()}, Fuel Type: {self.fuel_type}'
vehicle=Vehicle('Audi','A7')
print(vehicle.get_info())
car=Car('Ford','Raptor','Diesel')
print(car.get_info())