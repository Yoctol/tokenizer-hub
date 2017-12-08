from nltk.tokenize import WordPunctTokenizer, word_tokenize
    

class NltkTokenizer(object):
    
    def __init__(self):
        self.WPtokenizer = WordPunctTokenizer()
        
    def lcut(self, sentence, punct=True):
        sentence = sentence.lower()
        if punct == True:
            return(self.WPtokenizer.tokenize(sentence))
        else:
            return(word_tokenize(sentence))