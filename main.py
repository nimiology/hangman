import csv, sys, time, random
from os import system, name

HANGMAN1 = '-------\n|     |\n|     |\n|\n|\n|\n|\n|\n__________'
HANGMAN2 = '-------\n|     |\n|     |\n|     0\n|\n|\n|\n|\n|\n__________'
HANGMAN3 = '-------\n|     |\n|     |\n|     0\n|     |\n|\n|\n|\n|\n__________'
HANGMAN4 = '-------\n|     |\n|     |\n|     0\n|    /|\n|\n|\n|\n|\n__________'
HANGMAN5 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|\n|\n|\n__________'
HANGMAN6 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|    /\n|\n|\n__________'
HANGMAN7 = '-------\n|     |\n|     |\n|     0\n|    /|\\\n|    / \\\n|\n|\n__________'

FILE = open("WORDS.csv","r")
LISTWORDS = list(csv.reader(FILE))

class wordchooser:
    def __init__(self):
        self.NUM = random.randint(0,len(LISTWORDS[0]))
        self.WORD = LISTWORDS[0][self.NUM]
        self.COUNT = 0
        self.HIDE = len(self.WORD) * '_ ,'
        self.HIDED = self.HIDE.split(",")
        self.ALPHBAS = "    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P\n            Q, R, S, T, U, V, W, X, Y, Z"

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def hangman(self):
        self.clear()
        print()
        count = self.COUNT
        if count==0:
            print(HANGMAN1)
        elif count==1:
            print(HANGMAN2)
        elif count==2:
            print(HANGMAN3)
        elif count==3:
            print(HANGMAN4)
        elif count==4:
            print(HANGMAN5)
        elif count==5:
            print(HANGMAN6)
        elif count==6:
            print(HANGMAN7)
            print(self.WORD)
            print("YOU DIED!")

            self.retry()


    def input(self):
        self.CHOOSED = []
        self.POSITION = 0
        DELETER = input()
        DELETER2 = DELETER.upper()
        self.ALPHBAS = self.ALPHBAS.replace(DELETER2, " ")
        if len(DELETER)<2:
            if self.WORD.find(DELETER)>-1 or self.WORD.find(DELETER2)>-1:
                try:
                    while(self.POSITION<= len(self.WORD)):
                        self.POSITION = self.WORD.index(DELETER,self.POSITION)
                        self.CHOOSED.append(self.POSITION)
                        self.POSITION+=1
                except:
                    pass
                for letterreplace in self.CHOOSED:
                    self.HIDED[letterreplace] = DELETER
            else:
                self.COUNT +=1
        else:
            try:
                SHITISM = input("Just one word each time(Press enter to Continue)")
                pass
            except:
                pass

    def show(self):
        self.hangman()
        print(self.ALPHBAS)
        print("".join(self.HIDED))
        self.input()

    def retry(self):
        CONTINUE = int(input("If you want to try again enter 1 ,if you not enter0\n"))
        if CONTINUE == 0:
            exit()
        elif CONTINUE == 1:
            letsdoit()

    def start(self):
        def listtostr(HIDED):
            str = ""
            for meow in HIDED:
                str+=meow
            return str
        while True:
            if self.WORD==listtostr(self.HIDED):
                print('NICE')
                break
            else:
                self.show()
        self.retry()


def letsdoit():
    ob = wordchooser()
    ob.start()
letsdoit()

