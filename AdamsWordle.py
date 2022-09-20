import enchant
import enchant.checker

import tkinter as tk
import tkinter as ttk
from tkinter import *

from random_word import RandomWords

LARGE_FONT_STYLE = ("Times", 20, "bold")
DEFAULT_FONT_STYLE = ("Times", 25, "bold")
HEADER_FONT_STYLE = ("Montserrat", 40, "bold")
INF_FONT_STYLE = ("Montserrat", 18, "bold")


class AdamsWordle:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Adams W O R D L E")
        self.window.geometry("400x667")
        self.window.minsize(400, 667)
        self.window.resizable(False, False)
        self.window.configure(bg="#CCD1D1")
        self.d = enchant.Dict("en_UK")

        self.var = []
        self.max_len = 5
        self.min_len = 5
        self.round = 0
        self.deltaround = 0
        self.count = 0
        self.randomWord = self.randomWordGenerating()
        self.exp = ""
        self.c = 0
        self.g = []
        self.wor = []
        self.buttons = {}
        self.keyWidth = 30
        self.keyHeight = 40

        # HEADER:
        self.header = tk.Label(self.window, compound=tk.CENTER, font=HEADER_FONT_STYLE, bg="#CCD1D1",
                               text="W-O-R-D-L-E")
        self.header.place(x=16, y=2)

        # The individual labels for each word 6 columns (goes) and 5 rows (letters)
        self.textTest11 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest11.place(x=25, y=125, width=50, height=40)

        self.textTest12 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest12.place(x=100, y=125, width=50, height=40)

        self.textTest13 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest13.place(x=175, y=125, width=50, height=40)

        self.textTest14 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest14.place(x=250, y=125, width=50, height=40)

        self.textTest15 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest15.place(x=325, y=125, width=50, height=40)

        self.textTest21 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest21.place(x=25, y=175, width=50, height=40)

        self.textTest22 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest22.place(x=100, y=175, width=50, height=40)

        self.textTest23 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest23.place(x=175, y=175, width=50, height=40)

        self.textTest24 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest24.place(x=250, y=175, width=50, height=40)

        self.textTest25 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest25.place(x=325, y=175, width=50, height=40)

        self.textTest31 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest31.place(x=25, y=225, width=50, height=40)

        self.textTest32 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest32.place(x=100, y=225, width=50, height=40)

        self.textTest33 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest33.place(x=175, y=225, width=50, height=40)

        self.textTest34 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest34.place(x=250, y=225, width=50, height=40)

        self.textTest35 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest35.place(x=325, y=225, width=50, height=40)

        self.textTest41 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest41.place(x=25, y=275, width=50, height=40)

        self.textTest42 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest42.place(x=100, y=275, width=50, height=40)

        self.textTest43 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest43.place(x=175, y=275, width=50, height=40)

        self.textTest44 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest44.place(x=250, y=275, width=50, height=40)

        self.textTest45 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest45.place(x=325, y=275, width=50, height=40)

        self.textTest51 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest51.place(x=25, y=325, width=50, height=40)

        self.textTest52 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest52.place(x=100, y=325, width=50, height=40)

        self.textTest53 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest53.place(x=175, y=325, width=50, height=40)

        self.textTest54 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest54.place(x=250, y=325, width=50, height=40)

        self.textTest55 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest55.place(x=325, y=325, width=50, height=40)

        self.textTest61 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest61.place(x=25, y=375, width=50, height=40)

        self.textTest62 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest62.place(x=100, y=375, width=50, height=40)

        self.textTest63 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest63.place(x=175, y=375, width=50, height=40)

        self.textTest64 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest64.place(x=250, y=375, width=50, height=40)

        self.textTest65 = tk.Label(self.window, font=LARGE_FONT_STYLE, borderwidth=3, relief="solid", bg="White")
        self.textTest65.place(x=325, y=375, width=50, height=40)

        # Working GUI qwerty keyboard:
        self.buttons = {
            'Q': ttk.Button(self.window, text='Q', borderwidth=2, relief="solid", command=lambda: self.press('Q')),
            'W': ttk.Button(self.window, text='W', borderwidth=2, relief="solid", command=lambda: self.press('W')),
            'E': ttk.Button(self.window, text='E', borderwidth=2, relief="solid", command=lambda: self.press('E')),
            'R': ttk.Button(self.window, text='R', borderwidth=2, relief="solid", command=lambda: self.press('R')),
            'T': ttk.Button(self.window, text='T', borderwidth=2, relief="solid", command=lambda: self.press('T')),
            'Y': ttk.Button(self.window, text='Y', borderwidth=2, relief="solid", command=lambda: self.press('Y')),
            'U': ttk.Button(self.window, text='U', borderwidth=2, relief="solid", command=lambda: self.press('U')),
            'I': ttk.Button(self.window, text='I', borderwidth=2, relief="solid", command=lambda: self.press('I')),
            'O': ttk.Button(self.window, text='O', borderwidth=2, relief="solid", command=lambda: self.press('O')),
            'P': ttk.Button(self.window, text='P', borderwidth=2, relief="solid", command=lambda: self.press('P')),
            'A': ttk.Button(self.window, text='A', borderwidth=2, relief="solid", command=lambda: self.press('A')),
            'S': ttk.Button(self.window, text='S', borderwidth=2, relief="solid", command=lambda: self.press('S')),
            'D': ttk.Button(self.window, text='D', borderwidth=2, relief="solid", command=lambda: self.press('S')),
            'F': ttk.Button(self.window, text='F', borderwidth=2, relief="solid", command=lambda: self.press('F')),
            'G': ttk.Button(self.window, text='G', borderwidth=2, relief="solid", command=lambda: self.press('G')),
            'H': ttk.Button(self.window, text='H', borderwidth=2, relief="solid", command=lambda: self.press('H')),
            'J': ttk.Button(self.window, text='J', borderwidth=2, relief="solid", command=lambda: self.press('J')),
            'K': ttk.Button(self.window, text='K', borderwidth=2, relief="solid", command=lambda: self.press('K')),
            'L': ttk.Button(self.window, text='L', borderwidth=2, relief="solid", command=lambda: self.press('L')),
            'Z': ttk.Button(self.window, text='Z', borderwidth=2, relief="solid", command=lambda: self.press('Z')),
            'X': ttk.Button(self.window, text='X', borderwidth=2, relief="solid", command=lambda: self.press('X')),
            'C': ttk.Button(self.window, text='C', borderwidth=2, relief="solid", command=lambda: self.press('C')),
            'V': ttk.Button(self.window, text='V', borderwidth=2, relief="solid", command=lambda: self.press('V')),
            'B': ttk.Button(self.window, text='B', borderwidth=2, relief="solid", command=lambda: self.press('B')),
            'N': ttk.Button(self.window, text='N', borderwidth=2, relief="solid", command=lambda: self.press('N')),
            'M': ttk.Button(self.window, text='M', borderwidth=2, relief="solid", command=lambda: self.press('M'))
        }

        self.buttons['Q'].place(x=25, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['W'].place(x=60, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['E'].place(x=95, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['R'].place(x=130, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['T'].place(x=165, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['Y'].place(x=200, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['U'].place(x=235, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['I'].place(x=270, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['O'].place(x=305, y=430, width=self.keyWidth, height=self.keyHeight)
        self.buttons['P'].place(x=340, y=430, width=self.keyWidth, height=self.keyHeight)

        self.buttons['A'].place(x=42.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['S'].place(x=77.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['D'].place(x=112.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['F'].place(x=147.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['G'].place(x=182.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['H'].place(x=217.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['J'].place(x=252.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['K'].place(x=287.5, y=480, width=self.keyWidth, height=self.keyHeight)
        self.buttons['L'].place(x=322.5, y=480, width=self.keyWidth, height=self.keyHeight)

        self.buttons['Z'].place(x=77.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['X'].place(x=112.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['C'].place(x=147.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['V'].place(x=182.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['B'].place(x=217.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['N'].place(x=252.5, y=530, width=self.keyWidth, height=self.keyHeight)
        self.buttons['M'].place(x=287.5, y=530, width=self.keyWidth, height=self.keyHeight)


        # Button to check if the word is correct:

        self.check = Button(self.window, text='CHECK !', borderwidth=3, relief="solid", command=self.addTheWords)
        self.check.place(x=30, y=600, width=150, height=40)

        #  Button to start new game at any point of the game:

        self.new_try = Button(self.window, text='New Try', borderwidth=3, relief="solid", command=self.newGame)
        self.new_try.place(x=220, y=600, width=150, height=40)

        # Function enabling all the physical keys:
        self.bind_keys()


    def clear_boxes(self):
        """
        Function which clears all the boxes in the game every time there is new game button iniciated.
        """
        self.textTest11.config(text=" ", bg="White")
        self.textTest12.config(text=" ", bg="White")
        self.textTest13.config(text=" ", bg="White")
        self.textTest14.config(text=" ", bg="White")
        self.textTest15.config(text=" ", bg="White")
        self.textTest21.config(text=" ", bg="White")
        self.textTest22.config(text=" ", bg="White")
        self.textTest23.config(text=" ", bg="White")
        self.textTest24.config(text=" ", bg="White")
        self.textTest25.config(text=" ", bg="White")
        self.textTest31.config(text=" ", bg="White")
        self.textTest32.config(text=" ", bg="White")
        self.textTest33.config(text=" ", bg="White")
        self.textTest34.config(text=" ", bg="White")
        self.textTest35.config(text=" ", bg="White")
        self.textTest41.config(text=" ", bg="White")
        self.textTest42.config(text=" ", bg="White")
        self.textTest43.config(text=" ", bg="White")
        self.textTest44.config(text=" ", bg="White")
        self.textTest45.config(text=" ", bg="White")
        self.textTest51.config(text=" ", bg="White")
        self.textTest52.config(text=" ", bg="White")
        self.textTest53.config(text=" ", bg="White")
        self.textTest54.config(text=" ", bg="White")
        self.textTest55.config(text=" ", bg="White")
        self.textTest61.config(text=" ", bg="White")
        self.textTest62.config(text=" ", bg="White")
        self.textTest63.config(text=" ", bg="White")
        self.textTest64.config(text=" ", bg="White")
        self.textTest65.config(text=" ", bg="White")



    def addTheWords(self):
        """
        Function which is called everytime the check button is pressed.
        Function first checks if the randomly generated word is actually from en_UK dictionary
        If it is then it checks if the lenght of the entered word is 5 words and if the entered word is an actual english
        word spelled properly.
        If it is not spelled properly it informs the player that it is not an actual word and to fix the input.
        Finally, it also informs the player that if the entered word is not 5 words, it is too short.
        """
        self.string_name = ""

        for c in self.var:
            self.string_name += c
        while self.d.check(self.randomWord) is False:
            self.randomWordGenerating()
            self.addTheWords()

        if len(self.string_name) == self.max_len and self.d.check(self.string_name) is True:
            self.win(self.string_name)
            self.countTimes()

        if self.d.check(self.string_name) is False:
            self.initiate_inf_label("initiate")
            self.infLabel.config(text='Not a word', bg="#D21E1E")

        if len(self.string_name) != self.max_len:
            self.initiate_inf_label("initiate")
            self.infLabel.config(text=' Too Short ', bg="#D21E1E", fg="black")

    def win(self, word):
        """
        Function called after successfull check of the word in function add_the_word which first checks if the
        entered word is a match with the guess word.

        If it is not a match then it will clear the variables and call the function word_check to check individual
        letters, in the entered word.

        If  the word being checked is at its last sixth attempt, the game will initiate function game_lost which will
        inform the gamer they lost and what was the correct word.
        """
        self.initiate_inf_label("initiate")

        if self.randomWord == word:
            self.word_check(word, self.randomWord)
            self.infLabel.config(text=' CORRECT ', bg="green", fg="black")
            self.window.unbind("<Return>")
            self.window.unbind("<BackSpace>")

        if self.randomWord != word:
            self.wor.clear()
            for key, letter in self.letters.items():
                self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))
            self.word_check(word, self.randomWord)
            self.clearword()
            self.clearentries()
            self.machinecounter()
            self.infLabel.config(text='Not quite', bg="#D21E1E")

        if self.round == 5:
            self.gameLost()



    def word_check(self, list1, random):
        """
        Function which takes a generated word and the user imputed word and checks if they are equal and if not
        then it compares every letter.
        If the letters match it will initiate function boxer which then will change the box colour to either green,
        orange or gray.
        """

        n = len(list1)

        self.forbidden = []

        for item1, item2 in zip(list1, random):

            for i in range(n):
                if item1 == item2:
                    self.changeColour(item1, "green")
                    self.forbidden.insert(i, item1)
                    self.boxer(self.count, item1, "green")
                    self.count = self.count + 1

                elif item1 in random and item1 not in self.forbidden:
                    self.changeColour(item1, "orange")
                    self.boxer(self.count, item1, "orange")
                    self.count = self.count + 1

                elif item1 in random and item1 in self.forbidden:
                    self.boxer(self.count, item1, "orange")
                    self.count = self.count + 1

                elif item1 not in random:
                    self.changeColour(item1, "gray")
                    self.boxer(self.count, item1, "gray")
                    self.count = self.count + 1
        self.clearCounts()

    def newGame(self):
        """
        Function initates new game by rebinding the keyboard keys , clearing all variables and generating new guess word.
        """
        self.infLabel.config(text=' ', bg="#CCD1D1", borderwidth=0, relief="solid")

        self.bind_keys()

        self.clean_key()
        self.clearTimes()
        self.cleardeltarounds()
        self.clear_boxes()
        self.c = 0
        self.clearword()
        self.clearentries()
        self.wor.clear()
        self.var.clear()
        self.randomWord = self.randomWordGenerating()

    def randomWordGenerating(self):
        """
        Function which generates new random word from imported python module random_words()
        It also makes sure that the variable is not initiated as none to avoid error.
        """
        self.r = RandomWords()
        true_word = self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                           minDictionaryCount=3, minLength=5, maxLength=5)

        while true_word == None or '-' in true_word:
            true_word = self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                               minDictionaryCount=3, minLength=5, maxLength=5).upper()
        else:
            return true_word.upper()

    def initiate_inf_label(self, argument):
        """
        Function which initiates information banner label whitch always appears after the check button is being pressed.
        There is either option to initiate it or to destroy it so it disappears.

        """
        if argument == "initiate":
            self.infLabel = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
            self.infLabel.place(x=50, y=75, width=300, height=35)
        elif argument == "destroy" and self.deltaround >= 0:
            self.infLabel.after(1000, self.infLabel.destroy())

    def changeColour(self, widget, colr):
        """
        Function whic changes the color of the GUI keys based on the results of checks between the entered word and
        randomly generated word.
        Every letter is cross-checked with other letter in same location.

        If the letter is identical, then the key will be coloured green, if it is not identical, but it is present
        in the generated word it will be coloured orange and if it is not present in the generated word it will be
        coloured gray.
        """

        if colr == "green":
            self.buttons[widget].config(bg='green', fg='black')

            self.g.append(widget)

        if colr == "orange":
            self.buttons[widget].config(bg='yellow', fg='black')

        if colr == "gray":
            self.buttons[widget].config(bg='gray', fg='black')

    def countTimes(self):
        """
        Simple function counting rounds.
        """

        self.round = self.round + 1

    def machinecounter(self):
        """
        Function which adds counts for the deltaround variable.
        """
        self.deltaround = self.deltaround + 1

    def cellcounttimes(self, command):
        """
        Function which either adds or subtracts from c variable which is used to know to what label box should the
        letter be entered in.
        """
        if command == "plus":
            self.c = self.c + 1
        elif self.c >= 1 and command == "minus":
            self.c = self.c - 1
        else:
            self.c = 0

    def clearentries(self):
        """
        Function resetting the c variable to zero.
        """

        self.c = 0

    def clearTimes(self):
        """
        Function resetting the round variable to zero.
        """

        self.round = 0

    def cleardeltarounds(self):
        """
        Function resetting the deltaround variable to zero.
        """
        self.deltaround = 0

    def clearCounts(self):
        """
        Function reseting the count variable to zero.
        """
        self.count = 0

    def clearword(self):
        """
        Function resetting the var variable to empty.
        """
        self.var = []

    def clean_key(self):
        """
        Function which resets the GUI key button to white .
        """
        for key in self.buttons:
            self.buttons[key].config(bg='#f8f4f4', fg='black')

    def do_backspace(self):
        """
        Function which enables backspace key to delete the letters in the boxes and also update the
        variables so the game works as intended.
        """
        if self.c >= 0:
            self.cellcounttimes("minus")
            self.deltaboxes(self.c, " ")
            self.cellcounttimes("minus")
            self.wor = self.wor[:-1]
            self.var = self.var[:-1]
            for key, letter in self.letters.items():
                self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))

    def bind_keys(self):
        """
        Function which binds keys for qwerty keyboard and the enter key and bakcspace key.
        """

        self.letters = {"Q": "q", "W": "w", "E": "e", "R": "r", "T": "t", "Y": "y", "U": "u", "I": "i", "O": "o",
                        "P": "p",
                        "A": "a", "S": "s"
            , "D": "d", "F": "f", "G": "g", "H": "h", "J": "j", "K": "k", "L": "l", "Z": "z", "X": "x", "C": "c",
                        "V": "v", "B": "b"
            , "N": "n", "M": "m"}
        self.window.bind("<Return>", lambda event: self.addTheWords())
        self.window.bind("<BackSpace>", lambda event: self.do_backspace())

        for key, letter in self.letters.items():
            self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))

    #  Function which enables press of the qwerty keys to be added to the word string.
    def press(self, num):
        """
        Function which enables press of the qwerty keys to be added to the word string..
        """
        self.exp = str(num)
        self.deltaboxes(self.c, self.exp)
        self.var.append(self.exp)


    def combineletters(self, word):
        """
        Function which is called everytime any of the qwerty keys is pressed on psychical keyboard and then adds the key
        to the variable with 5 letters which is then tested against the actual random word generated.
        """
        if len(self.wor) < 5:
            self.deltaboxes(self.c, word)
            self.wor.append(word)
            self.var.append(word)
        if len(self.wor) == 5:
            self.wor.clear()
            for key, letter in self.letters.items():
                self.window.unbind(str(letter))


    def boxer(self, item, letter, colour):
        """
        Function which takes three arguments, item represents the position nof the box in the row ( 0 to 4 ),
        letter which represents the actual letter being inserted to the box and colour in which the box will be colored in.

        There is check for variable round which is changed everytime one word is checked from 0 to 5 ( 6 goes )

        """

        if item == 0:
            if self.round == 0:
                self.textTest11.config(text=letter, bg=colour)
            if self.round == 1:
                self.textTest21.config(text=letter, bg=colour)
            if self.round == 2:
                self.textTest31.config(text=letter, bg=colour)
            if self.round == 3:
                self.textTest41.config(text=letter, bg=colour)
            if self.round == 4:
                self.textTest51.config(text=letter, bg=colour)
            if self.round == 5:
                self.textTest61.config(text=letter, bg=colour)

        if item == 5:
            if self.round == 0:
                self.textTest12.config(text=letter, bg=colour)
            if self.round == 1:
                self.textTest22.config(text=letter, bg=colour)
            if self.round == 2:
                self.textTest32.config(text=letter, bg=colour)
            if self.round == 3:
                self.textTest42.config(text=letter, bg=colour)
            if self.round == 4:
                self.textTest52.config(text=letter, bg=colour)
            if self.round == 5:
                self.textTest62.config(text=letter, bg=colour)

        if item == 10:
            if self.round == 0:
                self.textTest13.config(text=letter, bg=colour)
            if self.round == 1:
                self.textTest23.config(text=letter, bg=colour)
            if self.round == 2:
                self.textTest33.config(text=letter, bg=colour)
            if self.round == 3:
                self.textTest43.config(text=letter, bg=colour)
            if self.round == 4:
                self.textTest53.config(text=letter, bg=colour)
            if self.round == 5:
                self.textTest63.config(text=letter, bg=colour)

        if item == 15:
            if self.round == 0:
                self.textTest14.config(text=letter, bg=colour)
            if self.round == 1:
                self.textTest24.config(text=letter, bg=colour)
            if self.round == 2:
                self.textTest34.config(text=letter, bg=colour)
            if self.round == 3:
                self.textTest44.config(text=letter, bg=colour)
            if self.round == 4:
                self.textTest54.config(text=letter, bg=colour)
            if self.round == 5:
                self.textTest64.config(text=letter, bg=colour)

        if item == 20:
            if self.round == 0:
                self.textTest15.config(text=letter, bg=colour)
            if self.round == 1:
                self.textTest25.config(text=letter, bg=colour)
            if self.round == 2:
                self.textTest35.config(text=letter, bg=colour)
            if self.round == 3:
                self.textTest45.config(text=letter, bg=colour)
            if self.round == 4:
                self.textTest55.config(text=letter, bg=colour)
            if self.round == 5:
                self.textTest65.config(text=letter, bg=colour)
                self.gameLost()



    def deltaboxes(self, item, letter):
        """
        Similar function to boxer() function but this one is only concerned with entries before every check is made.
        """

        if item == 0:

            if self.deltaround == 0:
                self.textTest11.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 1:
                self.textTest21.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 2:
                self.textTest31.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 3:
                self.textTest41.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 4:
                self.textTest51.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 5:
                self.textTest61.config(text=letter)
                self.cellcounttimes("plus")

        if item == 1:
            if self.deltaround == 0:
                self.textTest12.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 1:
                self.textTest22.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 2:
                self.textTest32.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 3:
                self.textTest42.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 4:
                self.textTest52.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 5:
                self.textTest62.config(text=letter)
                self.cellcounttimes("plus")

        if item == 2:
            if self.deltaround == 0:
                self.textTest13.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 1:
                self.textTest23.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 2:
                self.textTest33.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 3:
                self.textTest43.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 4:
                self.textTest53.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 5:
                self.textTest63.config(text=letter)
                self.cellcounttimes("plus")

        if item == 3:
            if self.deltaround == 0:
                self.textTest14.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 1:
                self.textTest24.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 2:
                self.textTest34.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 3:
                self.textTest44.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 4:
                self.textTest54.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 5:
                self.textTest64.config(text=letter)
                self.cellcounttimes("plus")

        if item == 4:

            if self.deltaround == 0:
                self.textTest15.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 1:
                self.textTest25.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 2:
                self.textTest35.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 3:
                self.textTest45.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 4:
                self.textTest55.config(text=letter)
                self.cellcounttimes("plus")
            if self.deltaround == 5:
                self.textTest65.config(text=letter)
                self.cellcounttimes("plus")

    def gameLost(self):
        """
        Function which is initiated after the games finishes their 6th go.
        It informs of the word and then resets the game .

        """
        self.infLabel.config(text="The word was: " + self.randomWord, bg="white", fg="red")
        for key, letter in self.letters.items():
            self.window.unbind(str(letter))
        self.window.unbind("<Return>")
        self.window.unbind("<BackSpace>")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    aWordle = AdamsWordle()
    aWordle.run()
