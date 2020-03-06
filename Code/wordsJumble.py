from hashtable import HashTable


class Jumble(object):
    def __init__(self, words):
        '''Create  a hash table and gets individual words. 
        adds words that are
        the same length of scramble'''
        self.words = words
        self.hash = HashTable()
        length = []
        for scrambled_word in words:
            if len(scrambled_word) not in length:
                length.append(len(scrambled_word))
        
        with open("/usr/share/dict/words", 'r') as file:
            for word in file:
                word = word.strip().lower() 
                if len(word) in length:
                    self.hash.set(word, word)
    
    def find_permutation(self, scrambled_word):
        '''get all possible permutation'''
        permutation = []

        if len(scrambled_word) == 1:
            return scrambled_word
        else:
            for char in scrambled_word:
                # Replcaes scramvbled letters until down to a single letter
                for string in self.find_permutation(scrambled_word.replace(char, "", 1)):
                    if (char + string) not in permutation:
                        permutation.append(char + string)
        return permutation


    def find_word(self, permutations):
        for perm in permutations:
            if self.hash.contains(perm):
                return self.hash.get(perm)
        return "word not Found"


    def unscramble(self):
        unscrabled = []
        for word in self.words:
            unscrabled.append(self.find_word(self.find_permutation(word)))
        
        return unscrabled
def main(scrambled_words_uppers):
    scrambled_words = map(lambda words:words.lower(),scrambled_words_uppers)
    jumble = Jumble(scrambled_words)
    return jumble.unscramble()

        


if __name__ == '__main__':
    result = main(['LAISA', 'LAURR', 'BUREEK', 'PROUOT'])
    result = main(['TARFD', 'JOBUM', 'TENJUK', 'LETHEM'])
    print(result)