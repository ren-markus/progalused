class Ristkylik:
    def__init__(self, pikkus, laius):
        self.pikkus = pikkus
        self.laius = laius
        
    def pindala (self):
        return self.pikkus * self.laius
    
Ristkylik = Ristkylik(5,2)
print(Ristkylik.pikkus, Ristkylik.laius)
print(Ristkylik.pindala())
