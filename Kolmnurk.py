class Kolmnurk:
    def __init__(self, kaatet, alus):
        self.kaatet = kaatet
        self.alus = alus
        
    def pindala(self):
        return self.alus * self.kaatet / 2
    
Kolmnurk = Kolmnurk(6,10)
print(Kolmnurk.alus, Kolmnurk.kaatet)
print(Kolmnurk.pindala())