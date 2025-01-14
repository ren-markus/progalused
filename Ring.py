import math


class Ring:
    def __init__(self, raadius):
        self.raadius = raadius
        
    def pindala (self):
        return self.raadius**2 * math.pi
    
ring = Ring(4)
print(ring.raadius, math.pi)
print(ring.pindala())