import letters as l
"""Stores information of all the players playing"""

players=[]
class Playerinfo(object):

    def __init__(self,name,score):
        """Define class
        :param name: str
        :param score:int
        :returns None"""
        self.name = name
        self.wordsavail=[]
        self.score=score
    
    def getName(self):
        """Function that takes input of player names and appends to list
        :returns appends name to players"""
        self.name=input("Enter player name: ")
        players.append(self.name)

    def get_score(self):
        """Getter function for score
        :returns int"""
        return self.score

    def set_score(self,number):
        """Setter function for score
        :returns int"""
        self.number = number
        self.score += self.number
        return self.score

    def wordsavail_method(self):
        """Function that stores all the letters available for each player
        :param wordsavail: list
        :returns list"""
        wordsavail=l.Letters.having_letters(self)
        return wordsavail

    def playerplaying(self):
        """Information of playing currently playing
        :returns player"""
        playing=0
        while playing<100:
            return player[playing]
            playing+=1
            if playing==4:
                playing=0

