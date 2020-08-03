class WordsCall(object):
    @staticmethod
    def wordread():
        with open ('words.txt') as words:
            wordlist = words.readlines()
            wordlist=[x.strip("\n").casefold() for x in wordlist]
            return wordlist

