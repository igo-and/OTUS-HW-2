import baseVehicle
import exception


class Plane(baseVehicle.Vehicle):


    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo ):
        super().__init__(weight, fuel, fuel_consumption )
        self.max_cargo = max_cargo
        self.cargo = cargo


    def load_cargo (self, new_cargo, cargo):
        cargo = cargo + new_cargo
        if cargo > self.max_cargo:
            raise exception.CargoOverload
        return print('Груз принят на борт')


    def remove_all_cargo (self, cargo):
        self.cargo = cargo
        cargo = 0


if __name__ == '__main__':
    plane_air = Plane(weight=10, fuel = 1100, fuel_consumption = 12, max_cargo = 4300, cargo= 1000 )
    plane_air.load_cargo(new_cargo= 700, cargo= 900)
    print(plane_air.__dict__)

    plane_air.remove_all_cargo(111)
