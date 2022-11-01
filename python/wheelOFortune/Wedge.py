import random
class Wedge():
    def __init__(self,t,round):
        if t == "br":
            self.type = "bankrupt"
            self.prize = 0
        elif t == "brm":
            self.type = "bankrupt W/ Million"
            self.prize = 1000000
        elif t == "lt":
            self.type = "lose a Turn"
            self.prize = 0
        elif t == "fp":
            self.type = "Free Play"
            self.prize = 0
        elif t == "w":
            self.type = "Wild"
            self.prize = 0
        elif t == "tp":
            self.type = "Top Prize"
            if round == 1:
                self.prize = 1500
            elif round == 2:
                self.prize = 2500
            elif round == 3:
                self.prize = 3500
            else:
                self.prize = 5000
        else:
            self.type = "Prize"
            self.prize = random.randint(10,19)*50
            
    def __str__(self):
        return(self.type+":\t\t"+str(self.prize))