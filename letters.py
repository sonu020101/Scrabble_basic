import random


class Letters(object):
    def __init__(self,owning_letters):
        self.owning_letters=owning_letters

    def having_letters(self):
        self.letter=[chr(c) for c in range(97, 123)]
        self.owning_letters=list()
        i=0
        while i<7:
            temp=random.choice(self.letter)
            if temp not in self.owning_letters:
                self.owning_letters.append(temp)
                i+=1
            else:
                continue
        return self.owning_letters

    def skip(self):
        self.owning_letters=list()
        for _ in range(7):
            self.owning_letters.append(random.choice(self.letter))
        return self.owning_letters



