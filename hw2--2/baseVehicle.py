import exception

class Vehicle:

    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, started):
        if started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise exception.LowFuelError


if __name__ == '__main__':
    #Проверяем метод start
    # наименование передаваемых переменных в экземпляр прописываю для удобства чтения кода
    excemp = Vehicle(weight = 8, fuel = 9, fuel_consumption = 10)
    print(f'атрибуты объекта {excemp.__dict__}')
    excemp.start(False)
