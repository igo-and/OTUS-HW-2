import baseVehicle
import exception


class Plane(baseVehicle.Vehicle):


    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo, distance ):
        super().__init__( weight, fuel, fuel_consumption, distance)
        self.max_cargo = max_cargo
        self.cargo = cargo
        self.tmp_cargo = self.cargo


    def load_cargo (self, new_cargo):
        self.cargo = self.cargo + new_cargo
        if self.cargo > self.max_cargo:
            raise exception.CargoOverload
        return print('Груз принят на борт')


    def remove_all_cargo (self):
        self.cargo = 0
        self.cargo = self.tmp_cargo


if __name__ == '__main__':
    plane_air = Plane(weight=10, fuel = 1100, fuel_consumption = 12, max_cargo = 4300, cargo= 1000, distance = 10 )
    plane_air.load_cargo(new_cargo= 700)
    print(plane_air.__dict__)

    plane_air.remove_all_cargo()
