from Wedge import Wedge
from random import shuffle,choice
class Wheel():
    def __init__(self,r):
        self.wedges = []
        self.wedges.append(Wedge("br",r))
        self.wedges.append(Wedge("brm",r))
        self.wedges.append(Wedge("lt",r))
        self.wedges.append(Wedge("fp",r))
        self.wedges.append((Wedge("tp",r)))
        self.wedges.append(Wedge("w",r))
        while len(self.wedges) < 24:
            self.wedges.append(Wedge("p",r))
        shuffle(self.wedges)
        
    def __str__(self):
        for wedge in self.wedges:
            print(wedge.type,str(wedge.prize))
        return ""
    
    def spin(self):
        return choice(self.wedges)