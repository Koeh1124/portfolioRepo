from random import choice
class Player():
    def __init__(self,name,bot):
        if not(bot):
            self.name = name
        else:
            with open("names.txt","r") as f:
                file = f.readlines
                names = []
                for line in file:
                    line = line.strip()
                    names.append(line)
                self.name = choice(names)
        self.total = 0
        self.cTotal = 0
        
    def bankrupt(self):
        self.cTotal = 0
        
    def endOfRound(self):
        self.total += self.cTotal
        self.cTotal = 0
        
    def win(self,prize):
        self.cTotal+=prize
        
    def __str__(self):
        return(f'''
Name:               {self.name}

Total earnings:     {self.total}
''')