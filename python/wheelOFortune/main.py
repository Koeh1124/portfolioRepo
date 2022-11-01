from Wheel import Wheel
from Player import Player

homeScree = f'''
        Welcome to 
    Wheel Of Fortune!
    
1) Play

2) How To Play

3) Leader Board

4) Credits

q) Quit
'''

howtoPlay  = '''

'''

creds = '''
Keenan:
-wheel
-catagories
-player class
-gussing logic(gussing letters and assigning proper scores)
-leaderboard

Aiden:
-selecting the puzzle
-displaying the puzzle
-How to play section

'''
def displayLeaderBoard():
    with open("leaderBoard.txt","r") as f:
        file = f.readlines()
        for line in file:
            print(line.strip())

def updateLeardBoard(playerList):
    pList = []
    for player in playerList:
        pList.append(player.name,player.score)
    scoreList = [player[1] for player in pList]
    with open("leaderBoard.txt","r") as f:
        file = f.readlines()
        for line in file:
            line = line.strip()
            player = int(line.split("-"))
            pList.append(player[0][3:-1],player[1][1:])
            scoreList.append(int(player[1][1:]))
        f.close()
    scoreList.sort()
    with open ("leaderBoard.txt","w") as f:
        if len(scoreList) > 5:
            topPlayers = []
            for i in range(5):
                for player in playerList:
                    if int(player[1]) == scoreList[i]:
                        topPlayers.append(player)
            for i in range(len(topPlayers)):
                f.write(f"{i}) {topPlayers[i][0]} - {topPlayers[i][1]}\n")
        else:
            topPlayers = []
            for score in scoreList:
                for player in pList:
                    if int(player[1]) == score:
                        topPlayers.append(player)
            for i in range(len(topPlayers)):
                f.write(f"{i}) {topPlayers[i][0]} - {topPlayers[i][1]}\n")

def makePlayers():
    print('''
    How many player do you have?

1) 1 player

2) 2 players

3) 3 players
''')
    
def main():
    ui = ""
    while ui != "q":
        while not(ui in ("q","1","2","3","4")):
            print(homeScree)
            ui = input("> ")
        if ui == "1":
            pass
        elif ui == "2":
            print(howtoPlay)
        elif ui == "3":
            print(creds)
        elif ui == "4":
            displayLeaderBoard()
        ui = ""
        
main()