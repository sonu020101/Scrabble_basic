import wordscall as wc
import Score as score
import playerinfo as pinfo
import letters as letters
import sys


class Playing(object):

    def __init__(self):
        self.word=""
        self.checklist=[]

    def set_word(self):
        self.word=input("\n Enter word")

    def letterlist(self):
        self.letter_list=pinfo.Playerinfo.wordsavail_method(self)
        self.checklist=self.letter_list

    def prinllist(self):
        for words in self.checklist:
            print(words,end='\t')

    def checkletter(self):
        self.lenofword=len(self.word)
        self.chword=list(self.word)
        self.count=0
        for x in self.chword:
            for y in self.checklist:
                if x==y:
                    self.count+=1
        if self.lenofword==self.count:
            return True
        else:
            return False


    def checkWord(self):
        self.round_score=0
        self.wordlist=wc.WordsCall.wordread()
        check=True
        if Playing.checkletter(self)==True:
            if self.word in self.wordlist:
                self.round_score=score.Score.correctans(self)
                pinfo.Playerinfo.set_score(self,self.round_score)
                check = False
            elif self.word not in self.wordlist:
                self.round_score=score.Score.wrong(self)
                pinfo.Playerinfo.set_score(self,self.round_score)
                check = False
        else:
            while check==True:
                if self.word=="":
                    print("Please enter a word empty block is not accepted")
                    Playing.set_word(self)
                    Playing.checkletter(self)
                    Playing.checkWord(self)
                elif self.word=="SKIP0".casefold():
                    self.round_score=score.Score.skipped(self)
                    pinfo.Playerinfo.set_score(self,self.round_score)
                    check=False
                elif self.word=="EXIT0".casefold():
                    print("Are you sure you want to end the game \n 1. Yes \n 2. No")
                    t=int(input())
                    if (t==1):
                        check=False
                        sys.exit()

                    if t==2:
                        Playing.set_word(self)
                        Playing.checkletter(self)
                        Playing.checkWord(self)
                else:
                    self.round_score=score.Score.wrong(self)
                    pinfo.Playerinfo.set_score(self,self.round_score)
                    check = False

        if(self.round_score==10):
            print("You got the right word, Your score has been incremented by 10 points")
        elif (self.round_score==0):
            print("You have choosed to skip the round, Your letters have been changed and their is no increment in "
                  "your points")
        else:
            print("We dont accept random words. Your score is decremented by 10 points")








