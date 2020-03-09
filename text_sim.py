
import spacy
nlp = spacy.load('en_core_web_md')
STOP_WORDS = spacy.lang.en.stop_words.STOP_WORDS

class String2Vector(): 
    def __init__(self,sentence, remove_stop_words=True, stop_words=STOP_WORDS, nlp=nlp):
        """
        Takes a text as input, do preprocessing, calculate vector representation and 
        return a spacy doc.
        INPUT: String, List, Series
        OUTPUT: Spacy Document 
        """

        self.sentence = sentence
        self.stop_words = stop_words 
        self.remove_stop_words = remove_stop_words
        self.spacy_doc = ''
        self.tokens = []
        self.nlp = nlp

    def convert_to_spacy_doc(self,sentence):
        if type(sentence) == str:
            self.spacy_doc=self.nlp(sentence)
            return self

        if type(sentence) == list:
            self.spacy_doc=self.nlp(' '.join(self.sentence))
            return self
    
    def process_sentence(self):
        self.convert_to_spacy_doc(self.sentence.lower())
       
        if self.remove_stop_words == True:
            self.tokens = [token.text for token in self.spacy_doc if token.text not in self.stop_words]
            self.spacy_doc = self.nlp(' '.join(self.tokens))

        return self.spacy_doc




