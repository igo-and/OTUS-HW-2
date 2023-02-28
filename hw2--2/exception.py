class LowFuelError(Exception):
    '''критически мало топлива в баке'''
    pass

class NotEnoughFuel(Exception):
    '''недостаточно топлива в баке'''
    pass

class CargoOverload(Exception):
    '''машина перегружена'''
    pass
