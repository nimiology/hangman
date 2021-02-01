import random
import time
import csv
import sys, time
HANGMAN1 = '-------\n|     |\n|     |\n|\n|\n|\n|\n|\n__________'
HANGMAN2 = '-------\n|     |\n|     |\n|     0\n|\n|\n|\n|\n|\n__________'
HANGMAN3 = '-------\n|     |\n|     |\n|     0\n|     |\n|\n|\n|\n|\n__________'
HANGMAN4 = '-------\n|     |\n|     |\n|     0\n|    /|\n|\n|\n|\n|\n__________'
HANGMAN5 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|\n|\n|\n__________'
HANGMAN6 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|    /\n|\n|\n__________'
HANGMAN7 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|    / \\\n|\n|\n__________'

FILE = open("WORDS.csv","r")
class wordchooser:
    def __init__(self,FILE):
        self.LISTWORDS = list(csv.reader(FILE))
        self.NUM = random.randint(0,len(self.LISTWORDS[0]))
        self.WORD = self.LISTWORDS[0][self.NUM]
        self.count = 0

    def hangman(self,count):
        if count==0:
            print(HANGMAN1)
        if count==1:
            print(HANGMAN2)
        if count==2:
            print(HANGMAN3)
        if count==3:
            print(HANGMAN4)
        if count==4:
            print(HANGMAN5)
        if count==5:
            print(HANGMAN6)
        if count==6:
            print(HANGMAN7)

    def shower(self):
        HIDED = len(self.WORD)*'_ '
        alphbas = ['A','B','C','D','E','F','G','H','I','J','K'
                     ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for alphba in alphbas:
            print(alphba)



ob = wordchooser(FILE)
ob.shower()

