from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import numpy as np
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from natsort import natsorted
import string
nltk.download('stopwords')


class Posting_List():
    """
    Posting List Implementation
    based on lines of file
    """
    def __init__(self,File_Name):
        self.file = open(File_Name,encoding="utf")
        self.read = self.file.read()
        self.file.seek(0)
        self.line = 1
        self.L_Array = []
        self.text_token =[]
        self.tokens_No_Stop = []
        self.List = {}

    def Line_Count(self):
        for word in self.read:
            if word == '\n':
                self.line += 1
        print("Number of lines in file is: ", self.line)

    def Line_Split(self):
        for i in range(self.line):
            self.L_Array.append(self.file.readline())

    def Punc_Remove(self):
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for ele in self.read:  
            if ele in punc:  
                self.read = self.read.replace(ele, " ") 

    def Tokenizer(self):
        for i in range(1):
            # this will convert
            # the word into tokens
            self.text_tokens = word_tokenize(self.read)

        self.tokens_No_Stop = [word for word in self.text_tokens if not word in stopwords.words()]

    def Post_List(self):
        for i in range(self.line):
            check = self.L_Array[i].lower()
            for item in self.tokens_No_Stop:
            
                if item in check:
                    if item not in self.List:
                        self.List[item] = []

                    if item in self.List:
                        self.List[item].append(i+1)
        print(self.List)
        
########################################################################################################
class Positional_Index():
    def __init__(self) :
        pass



if __name__ == "__main__":

    posting_list = Posting_List("file.txt")
    posting_list.Line_Count()
    posting_list.Line_Split()
    posting_list.Punc_Remove()
    posting_list.Tokenizer()
    posting_list.Post_List()
    