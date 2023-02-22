from dataclasses import dataclass
from typing import Any

@dataclass
class Engine:
    volume: Any = float
    pistons: Any = int

engine_car = Engine(3.8, 8)
print(engine_car.__dict__)