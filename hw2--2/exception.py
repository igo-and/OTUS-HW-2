class LowFuelError(Exception):
    '''критически мало топлива в баке'''

class NotEnoughFuel(Exception):
    '''недостаточно топлива в баке'''

class CargoOverload(Exception):
    '''машина перегружена'''
