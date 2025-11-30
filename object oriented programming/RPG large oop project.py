import random 
class Gamer:
    
    name:str = ""
    level:int = 0
    xp:int = 0

    def __init__(self,name,level,xp):
        if name != "":
            self.name = name
        else:
            print("Name cannot be empty")
            exit
        if level < 0:
            level = 0
        else:
            self.level = int(level)
        if xp < 0:
            self.xp = 0  
        else:
            self.xp = int(xp)
    
    def __str__(self):
        return ("User:"+self.name+"   level:"+str(self.level)+"   XP:"+str(self.xp))
    
    def gainxp(self,amount,placeholder,adding):
        if self.level < 0:
            self.level = 0
        if self.xp < 0:
            self.xp = 0
        oldlevel = self.level
        self.xp += amount
        placeholder = self.level
        self.level = self.xptolevel(self.xp)+placeholder
        if self.level > placeholder:
            self.xp = self.xp - 100*(self.level - placeholder)
        else:
            pass
        if not adding:
            exit
        if self.level > oldlevel:
            print("Level up! from",oldlevel,"to",self.level)
    
    def compare(self,other):
        if self.level > other.level:
            print(self.name,"is at a higher level than",other.name,"with",self.level,"vs",other.level)
        elif self.level < other.level:
            print(other.name,"is at a higher level than",self.name,"with",other.level,"vs",self.level)
        else:
            if self.xp > other.xp:
                print(self.name,"is at the same level as",other.name,"but has more XP with",self.xp,"vs",other.xp)
            elif self.xp < other.xp:
                print(other.name,"is at the same level as",self.name,"but has more XP with",other.xp,"vs",self.xp)
            else:
                print(self.name,"and",other.name,"are at the same level and have the same XP with level",self.level,"and XP",self.xp)

    @staticmethod
    def xptolevel(xp):
        return xp//100

class Game:
    #def __init__(self):

    @staticmethod
    def startdualplay(player1:Gamer,player2:Gamer,pointsforwin):
        print(player1.name,"vs",player2.name)
        print("Both players will pick a random number from 1-10, closest to the random number wins!")
        number = random.randint(1,10)
        player1.choice = int(input(player1.name+", pick a number between 1 and 10: "))
        player2.choice = int(input(player2.name+", pick a number between 1 and 10: "))
        print("The random number is:",number)
        if (player1.choice < 1 or player1.choice > 10) or (player2.choice < 1 or player2.choice > 10):
            print("Invalid choice(s). Choices must be between 1 and 10.")
        elif (number - player1.choice) < (number - player2.choice):
            print(player1.name,"wins! the random number was",number,"and their choice was",player1.choice,"vs",player2.choice)
            player1.gainxp(pointsforwin,0,False)
            player2.gainxp(-20,0,False)
            print(player1.name, "has gained",pointsforwin,"XP and is at",player1.xp,"XP and is at level",player1.level)
            print(player2.name, "has lost 20 XP and is at",player2.xp,"XP and is at level",player2.level)
        elif (number - player1.choice) > (number - player2.choice):
            print(player2.name,"wins! the random number was",number,"and their choice was",player2.choice,"vs",player1.choice)
            player2.gainxp(pointsforwin,0,False)
            player1.gainxp(-20,0,False)
            print(player2.name, "has gained",pointsforwin,"XP and is at",player2.xp,"XP and is at level",player2.level)
            print(player1.name, "has lost 20 XP and is at",player1.xp,"XP and is at level",player1.level)
        else:
            print("It's a tie! both players chose",player1.choice)
            print(player1.name, "remains at",player1.xp,"XP and is at level",player1.level)
            print(player2.name, "remains at",player2.xp,"XP and is at level",player2.level)
        again = input("Game over! Play again for double xp?(y/n)")
        if again.lower() in ("y","yes"):
            pointsforwin = 100
            again = True
        else:
            again = False
            pointsforwin = 50
            print("Thanks for playing!")
        return again, pointsforwin
    
    @staticmethod
    def startsingleplay(player1,pointsforwin,again):
        print(player1.name,"vs GameBot")
        print("Both players will pick a random number from 1-10, closest to the random number wins!")
        number = random.randint(1,10)
        player1.choice = int(input(player1.name+", pick a number between 1 and 10: "))
        botchoice = random.randint(1,10)
        print("The random number is:",number)
        if player1.choice < 1 or player1.choice > 10:
            print("Invalid choice. Choices must be between 1 and 10.")
        elif (number - player1.choice) < (number - botchoice):
            print(player1.name,"wins! the random number was",number,"and their choice was",player1.choice,"vs",botchoice)
            player1.gainxp(pointsforwin,0,False)
            print(player1.name, "has gained",pointsforwin,"XP and is at",player1.xp,"XP and is at level",player1.level)
        elif (number - player1.choice) > (number - botchoice):
            print("GameBot wins! the random number was",number,"and its choice was",botchoice,"vs",player1.choice)
            player1.gainxp(-20,0,False)
            print(player1.name, "has lost 20 XP and is at",player1.xp,"XP and is at level",player1.level)
        else:
            print("It's a tie! both players chose",player1.choice)
            print(player1.name, "remains at",player1.xp,"XP and is at level",player1.level)
        again = input("Game over! Play again for double xp?(y/n)")
        if again.lower() in ("y","yes"):
            pointsforwin = 100
            again = True
        else:
            again = False
            pointsforwin = 50
            print("Thanks for playing!")
        return again, pointsforwin
    
    def addplayer(name,level,xp):
        newplayer = Gamer(name,level,xp)
        global playerlist
        if level < 0:
            level = 0
        if xp < 0:
            xp = 0
        playerlist.append(newplayer)
        print("Player",name,"added!")

    def addplayers(continueadding):
        while continueadding.lower() == "y" or continueadding.lower() == "yes":
            name = input("Enter player name: ")
            if name in playerlist:
                print("Player already exists, please choose a different name.")
                continue
            else:
                level = int(input("Enter player level: "))
                xp = int(input("Enter player XP: "))
                Game.addplayer(name,level,xp)
                continueadding = input("Do you want to add another player? (y/n): ")
        return playerlist
    
    def findplayer(playername):
        global playerlist
        player1 = None
        for player in playerlist:
            if player.name == playername:
                player1 = player
                return player1
        print("Player not found.")       
        return None    
    
    def findplayers(player1name,player2name):
        global playerlist
        player1 = None
        player2 = None
        for player in playerlist:
            if player.name == player1name:
                player1 = player
            if player.name == player2name:
                player2 = player
        if player1 and player2:
            return player1,player2      
        return None,None

adding = True
gain = 0
pointsforwin = 50
again = False
placeholder = 0       
playerlist: list[Gamer] = []
continueadding = "y"       
print("Welcome to The Game Centre!")
print("First, let's add some players.")
Game.addplayers(continueadding)
for player in playerlist:
    player.gainxp(0,placeholder,True)
    print(player)
while True:
    choice = input("add player (a)| start single play (s)| start dual play (d)| compare players (c)|see player stats (p) exit: (e)")
    if choice.lower() == "a":
        continueadding = "y"
        Game.addplayers(continueadding)
        print("Current players:")
        for player in playerlist:
            Gamer.player.gainxp(0,placeholder,True)
            print(player)
    elif choice.lower() == "s":
        playername = input("Enter player name: ")
        for player in playerlist:
            if player.name == playername:
                while True:
                    again, pointsforwin = Game.startsingleplay(player,pointsforwin,again)
                    if not again:
                        break
                break
        else:
            print("Player not found.")
    elif choice.lower() == "d":
        player1,player2 = Game.findplayers(input("Enter first player name"),input("Enter second player name"))
        if player1 and player2:
            while True:
                again, pointsforwin = Game.startdualplay(player1,player2,pointsforwin)
                if not again:
                    break
        else:
            print("One or both players not found.")
    elif choice.lower() == "c":
        player1,player2 = Game.findplayers(input("Enter first player name"),input("Enter second player name"))
        if player1 and player2:
            player1.compare(player2)
        else:
            print("One or both players not found.")
    elif choice.lower() == "p":
        for player in playerlist:
            player.gainxp(0,placeholder,True)
            print(player)
    elif choice.lower() == "e":
        print("Exiting the Game Centre. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    






    
