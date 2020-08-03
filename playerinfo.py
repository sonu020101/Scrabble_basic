import letters as l

players=[]
class Playerinfo(object):

    def __init__(self,name,score):
        self.name = name
        self.wordsavail=[]
        self.score=score
    
    def getName(self):
        self.name=input("Enter player name: ")
        players.append(self.name)

    def get_score(self):
        return self.score

    def set_score(self,number):
        self.number = number
        self.score += self.number
        return self.score

    def wordsavail_method(self):
        wordsavail=l.Letters.having_letters(self)
        return wordsavail

    def playerplaying(self):
        playing=0
        while playing<4:
            return player[playing]
            playing+=1
            if playing==4:
                playing=0








