#Classes are blueprints for creating objects
class Vehichle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along...')
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehichle("Ford", "F150")
print(my_car.make)
print(my_car.model)
my_car.get_make_model()

your_car = Vehichle("Tesla", "Model X")
your_car.get_make_model()
your_car.moves()


#Inherits vehicle class. Other classes that can inherit from other classes
class Airplane(Vehichle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("Airplanes fly")

class Truck(Vehichle):
    def moves(self):
        print("Rumbles Along")

class GolfCart(Vehichle):
    pass

plane = Airplane("Boeing", "730", "13943")
ram = Truck("Dodge", "Ram")
wang = GolfCart("Cart", "124")

plane.moves()
print(plane.faa_id)
ram.get_make_model()
ram.moves()
wang.moves()



#Polymorphism. Ability to behave differently in response to the same input messages
for vehicle in (my_car, your_car, plane, ram, wang):
    vehicle.get_make_model()
    vehicle.moves()