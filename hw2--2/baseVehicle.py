import exception

class Vehicle:

    #started = False - перенёс в init

    def __init__(self, weight, fuel, fuel_consumption, distance, started = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.distance = distance
        self.started = started

    def start(self):
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise exception.LowFuelError


    # перенёс метод из Car
    def move(self):
        spend_fuel = self.distance * self.fuel_consumption
        if self.fuel < spend_fuel:
            raise exception.NotEnoughFuel
        else:
            print(f'наличие ДО поездки = {self.fuel}')
            self.fuel -= spend_fuel
            print(f'остаток после поездки = {self.fuel}' )


if __name__ == '__main__':
    #Проверяем метод start
    # наименование передаваемых переменных в экземпляр прописываю для удобства чтения кода
    examp = Vehicle(weight = 8, fuel = 9, fuel_consumption = 10, distance = 10, started = False)
    print(f'атрибуты объекта excemp {examp.__dict__}')
    examp.start()


