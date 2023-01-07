import random
class Player:
    def __init__(self, name):
        self.name=name
    def getmove(self,game):
        pass
            
class humanPlayer(Player):
    def __init__(self,name):
        super().__init__(name)
        
    def getmove(self,nbstick):
        choix=int(input("choose a number of  stick(1-3)"))

        while choix not in [1,2,3]:
            
            
            choix=input("choose a number of  stick(1-3) :")

        nbstick=nbstick-choix
        return nbstick
            
            
        



class robotPlayer(Player):
    def __init__(self,name):
        super().__init__(name)
        
    def getmove(self,nbstick):
       choix=random.choice([1,2,3]) 
       

       nbstick-=choix
       return nbstick