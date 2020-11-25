from functools import reduce


class Bet:
    
    def __init__(self, stakes=1, odds=[1], ew=True, ewterms=[0.25], winner=[True]):
        self.stakes = stakes
        self.odds = odds
        self.ew = ew
        self.winner = winner # win or place; win = True, place = False
        
        self.decodds = list(map(lambda x:x+1, odds))
        self.placeodds = list(map(lambda x,y : x*y+1,odds,ewterms))
        self.fullodds = reduce(lambda x,y:x*y, self.decodds)
        self.fullplaceodds = reduce(lambda x,y:x*y, self.placeodds)
        self.winpart = reduce(lambda x,y:x*y, self.winner)
    
    def totalstakes(self):
        return self.stakes + self.stakes*self.ew



class Accum(Bet):
    
    def __init__(self, stakes, odds, ew, ewterms, winner):
        Bet.__init__(self,stakes,odds,ew,ewterms,winner)
        
    def payout(self):
        return self.winpart*self.stakes*self.fullodds + self.ew*self.stakes*self.fullplaceodds

class Multiple(Accum):
    
    def __init__(self, stakes, odds, ew, ewterms, winner):
        Accum.__init__(self,stakes,odds,ew,ewterms,winner)
        
        self.bfsplusone = list(map(lambda x:x+1,self.decodds))
        self.fullbfspone = reduce(lambda x,y:x*y, self.bfsplusone)
        
        self.placebfplusone = list(map(lambda x:x+1, self.placeodds))
        self.fullplacebfspone = reduce(lambda x,y:x*y, self.placebfplusone)


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def choose(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def lucky15bets(selections=4):
    mysum = 0
    for i in range(1,selections+1):
        mysum += choose(selections,i)
    return mysum

def yankeebets(selections=4):
    mysum = 0
    for i in range(2,selections+1):
        mysum += choose(selections,i)
    return mysum

class LuckyFifteen(Multiple):
    
    def __init__(self, stakes, odds, ew, ewterms, winner):
        Multiple.__init__(self,stakes,odds,ew,ewterms,winner)
        
    def payout(self):
        return self.winpart*self.stakes*(self.fullbfspone-1) + self.ew*self.stakes*(self.fullplacebfspone-1)
    
    def totalstakes(self):
        return self.stakes*lucky15bets(len(self.odds)) + self.ew*self.stakes*lucky15bets(len(self.odds))

class Yankee(Multiple):
    
    def __init__(self, stakes, odds, ew, ewterms, winner):
        Multiple.__init__(self,stakes,odds,ew,ewterms,winner)
        
    def payout(self):
        return self.winpart*self.stakes*(self.fullbfspone-1-reduce(lambda x,y:x+y,self.decodds)) \
                + self.ew*self.stakes*(self.fullplacebfspone-1-reduce(lambda x,y:x+y,self.placeodds))
    
    def totalstakes(self):
        return self.stakes*yankeebets(len(self.odds)) + self.ew*self.stakes*yankeebets(len(self.odds))



        