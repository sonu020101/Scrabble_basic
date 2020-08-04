class WordsCall(object):
    """Class that gets all the words available in words.txt"""
    @staticmethod
    def wordread():
        with open ('words.txt') as words:
            wordlist = words.readlines()
            wordlist=[x.strip("\n").casefold() for x in wordlist]
            return wordlist
