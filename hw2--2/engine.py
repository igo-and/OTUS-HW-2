from dataclasses import dataclass

@dataclass
class Engine:
    volume: float = 1.5
    pistons: int = 4

engine = Engine(2.5, 6)
print(engine.__dict__)