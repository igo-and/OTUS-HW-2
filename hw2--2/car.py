from engine import Engine

class Car(Engine):

    def __init__(self, started, engine = Engine):
        super().__init__(started, engine)
        self.engine = engine

    def set_engine(self):
        print(f'установлен движок = {self.engine.__dict__}')


if __name__ == '__main__':
    examp2 = Car(True)
    examp2.set_engine()










