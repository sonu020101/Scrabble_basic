import playing as p
import playerinfo as pinfo

class Game(object):
    def __init__(self):
        self.name=""
        self.score=0

    def send_name(self):
        pinfo.Playerinfo.getName(self)

    def get_name(self):
        self.name=pinfo.Playerinfo.playerplaying(self)

    def get_score(self):
        self.score=pinfo.Playerinfo.get_score()

    def running(self):
        p.Playing.letterlist(self)
        p.Playing.prinllist(self)
        p.Playing.set_word(self)
        p.Playing.checkWord(self)

    def display(self):
        print(self.name + " is playing and player's current score is "+ str(self.score))


