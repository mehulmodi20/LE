import sys

class STROverload:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return "%s %s" % (self.word, "Mehul")
    

if __name__ == "__main__":
    word = sys.argv[1]
    s = STROverload(word)
    print(s)
    