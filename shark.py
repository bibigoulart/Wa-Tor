
from creature import Creature

class Shark(Creature):
    """Predators of Wa-Tor."""

    def __init__(self, x, y):
        self.handler = 2
        self.libido = 0
        self.energy = 6
        self.x = x
        self.y = y
        Creature.instances.append(self)
    
