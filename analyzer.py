import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        
        
        """Initialize Analyzer."""
        posfile = open(positives, "r")
        negfile = open(negatives, "r")
        p = posfile.readline()
        n = negfile.readline()
        self.postxt = ""
        self.negtxt = ""
        
        while p:
            if not p.startswith(";"):
                self.postxt += p
            p = posfile.readline()
        posfile.close()
        
        while n:
            if not n.startswith(";"):
                self.negtxt += n
            n = negfile.readline()
        negfile.close()
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        count = 0
        
        tokenizer = nltk.tokenize.TweetTokenizer()
        words = tokenizer.tokenize(text)
        for x in words:
            temp = x.lower() 
            if temp in self.postxt:
                count += 1
            elif temp in self.negtxt:
                count -= 1
            
        return count