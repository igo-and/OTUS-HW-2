import exception
import baseVehicle
import engine


class Car(baseVehicle.Vehicle, engine.Engine):

    def __init__(self, weight, fuel, fuel_consumption, distance):
        super().__init__(weight, fuel, fuel_consumption)
        self.distance = distance

    def move(self):
        spend_fuel = self.distance * self.fuel_consumption
        if self.fuel < spend_fuel:
            raise exception.NotEnoughFuel
        else:
            print(f'наличие ДО поездки = {self.fuel}')
            self.fuel -= spend_fuel
            print(f'остаток после поездки = {self.fuel}' )

    def set_engine(self, engine):
        engine_on_car = engine
        return engine_on_car


if __name__ == '__main__':
    exemp2 = Car(weight=10, fuel = 1100, fuel_consumption = 12, distance = 13)
    print(exemp2.__dict__)
    exemp2.move()









