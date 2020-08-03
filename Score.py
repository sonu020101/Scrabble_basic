class Score(object):
    def __init__(self):
        self.score = 0

    def correctans(self):
        self.score=0
        self.score+=10
        return self.score

    def skipped(self):
        self.score=0
        self.score+=0
        return self.score

    def wrong(self):
        self.score=0
        self.score-=10
        return self.score


