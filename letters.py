import random


class Letters(object):
    """Getting random letters and reutning them"""
    def __init__(self,owning_letters):
        self.owning_letters=owning_letters

    def having_letters(self):
        """Letters checked and added based on previous word
        :returns list"""
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
        """If person cant find a word with letters he is having he can can to chane his letter
        :returns list"""
        self.owning_letters=list()
        for _ in range(7):
            self.owning_letters.append(random.choice(self.letter))
        return self.owning_letters
