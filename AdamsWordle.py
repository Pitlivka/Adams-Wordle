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
        self.window.title("W O R D L E")
        self.window.geometry("400x667")
        self.window.minsize(400, 667)
        self.window.resizable(False, False)
        self.window.configure(bg="#CCD1D1")
        self.d = enchant.Dict("en_UK")
        max_len = 5
        min_len = 5
        self.var = []
        self.old_value = ''
        self.max_len = max_len
        self.min_len = min_len
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
        self.w = tk.Label(self.window, compound=tk.CENTER, font=HEADER_FONT_STYLE, bg="#CCD1D1", text="W O R D L E")
        self.w.place(x=25, y=2)
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

        self.buttons['Q'].place(x=25, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['W'].place(x=60, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['E'].place(x=95, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['R'].place(x=130, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['T'].place(x=165, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['Y'].place(x=200, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['U'].place(x=235, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['I'].place(x=270, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['O'].place(x=305, y=400, width=self.keyWidth, height=self.keyHeight)
        self.buttons['P'].place(x=340, y=400, width=self.keyWidth, height=self.keyHeight)

        self.buttons['A'].place(x=42.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['S'].place(x=77.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['D'].place(x=112.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['F'].place(x=147.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['G'].place(x=182.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['H'].place(x=217.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['J'].place(x=252.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['K'].place(x=287.5, y=450, width=self.keyWidth, height=self.keyHeight)
        self.buttons['L'].place(x=322.5, y=450, width=self.keyWidth, height=self.keyHeight)

        self.buttons['Z'].place(x=77.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['X'].place(x=112.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['C'].place(x=147.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['V'].place(x=182.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['B'].place(x=217.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['N'].place(x=252.5, y=500, width=self.keyWidth, height=self.keyHeight)
        self.buttons['M'].place(x=287.5, y=500, width=self.keyWidth, height=self.keyHeight)

        self.btn = Button(self.window, text='CHECK !', borderwidth=3, relief="solid", command=self.addTheWords)
        self.btn.place(x=30, y=580, width=150, height=40)

        self.hintBtn = Button(self.window, text='New Try', borderwidth=3, relief="solid",  command=self.newGame)
        self.hintBtn.place(x=220, y=580, width=150, height=40)

        self.bind_keys()

    def press(self, num):
        self.exp = str(num)

        self.deltaboxes(self.c, self.exp)
        self.var.append(self.exp)

    def combineletters(self, word):
        if len(self.wor) < 5:
            self.deltaboxes(self.c, word)
            self.wor.append(word)
            self.var.append(word)
        if len(self.wor) == 5:
            self.wor.clear()
            for key, letter in self.letters.items():
                self.window.unbind(str(letter))

    def clearBoxes(self):
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



    def addTheWords(self):
        self.string_name = ""

        for c in self.var:
            self.string_name += c
        while self.d.check(self.randomWord) is False:
            self.randomWordGenerating()
            self.addTheWords()

        if len(self.string_name) == self.max_len and self.d.check(self.string_name) is True :
            self.win(self.string_name)
            self.countTimes()

        if self.d.check(self.string_name) is False:
            self.initiate_inf_label("initiate")
            self.infLabel.config(text='Not a word', bg="#D21E1E")

        if len(self.string_name) != self.max_len:
            self.initiate_inf_label("initiate")
            self.infLabel.config(text=self.randomWord + ' Too Short ',bg= "#D21E1E", fg = "black")




    def win(self, word):
        self.initiate_inf_label("initiate")

        if self.randomWord == word:
            self.wordCheck(word, self.randomWord)
            self.infLabel.config(text=' CORRECT ',bg= "green", fg = "black")
            self.window.unbind("<Return>")
            self.window.unbind("<BackSpace>")


        if self.randomWord != word:
            self.wor.clear()
            for key, letter in self.letters.items():
                self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))
            self.wordCheck(word,self.randomWord)
            self.clearword()
            self.clearentries()
            self.machinecounter()
            self.infLabel.config(text='Not quite', bg="#D21E1E")



        if self.round == 4:
            self.gameLost()

    def newGame(self):
        self.infLabel.config(text=' ', bg="#CCD1D1" ,  borderwidth=0, relief="solid")

        self.bind_keys()

        self.cleanKey()
        self.clearTimes()
        self.cleardeltarounds()
        self.clearBoxes()
        self.c = 0
        self.clearword()
        self.clearentries()
        self.wor.clear()
        self.var.clear()
        self.randomWord = self.randomWordGenerating()

    def randomWordGenerating(self):
        self.r = RandomWords()
        true_word = self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                      minDictionaryCount=3, minLength=5, maxLength=5)

        while true_word == None or '-' in true_word:
            true_word = self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective",
                                          minDictionaryCount=3, minLength=5, maxLength=5).upper()
        else:
            return true_word.upper()


    def initiate_inf_label(self, argument):
        if argument == "initiate":
            self.infLabel = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
            self.infLabel.place(x=50, y=75, width=300, height=35)
        elif argument == "destroy" and self.deltaround >= 0:
            self.infLabel.after(1000, self.infLabel.destroy())


    def changeColour(self, widget, colr):


        if colr == "green" :
            self.buttons[widget].config( bg='green', fg='black')

            self.g.append(widget)

        if colr == "orange"  :
            self.buttons[widget].config(bg='yellow', fg='black')

        if colr == "gray" :
            self.buttons[widget].config(bg='gray', fg='black')


    def countTimes(self):

        self.round = self.round + 1


    def cellcounttimes(self, command):
        if command == "plus":
            self.c = self.c + 1
        elif self.c >= 1 and command == "minus":
            self.c = self.c - 1
        else:
            self.c = 0

    def clearentries(self):
        self.c = 0
    def clearTimes(self):

        self.round = 0

    def cleardeltarounds(self):
        self.deltaround = 0


    def clearCounts(self):
        self.count = 0
    def clearword(self):
        self.var =  []

    def cleanKey(self):
        for key in self.buttons:
            self.buttons[key].config(bg='#f8f4f4', fg='black')


    def wordCheck(self,list1,random):
        n = len(list1)

        self.forbidden =  []

        for item1, item2 in zip(list1, random):

            for i in range(n):
                if item1 == item2:

                    self.changeColour(item1,"green")
                    self.forbidden.insert(i, item1)
                    self.boxer(self.count, item1,"green")
                    self.count = self.count + 1

                elif item1 in random and item1 not in self.forbidden:

                    self.changeColour(item1, "orange")

                    self.boxer(self.count, item1, "orange")
                    self.count = self.count + 1

                elif item1 in random and item1  in self.forbidden:
                    self.boxer(self.count, item1, "orange")
                    self.count = self.count + 1


                elif item1 not in random:
                    self.changeColour(item1, "gray")
                    self.boxer(self.count, item1, "gray")
                    self.count = self.count + 1
        self.clearCounts()


    def boxer(self, item,letter,colour):

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
                self.gameLost()
                self.textTest55.config(text=letter, bg=colour)

    def do_backspace(self):
        if self.c >= 0:
            self.cellcounttimes("minus")
            self.deltaboxes(self.c, " ")
            self.cellcounttimes("minus")
            self.wor = self.wor[:-1]
            self.var = self.var[:-1]
            for key, letter in self.letters.items():
                self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))



    def bind_keys(self):


        self.letters = {"Q": "q", "W": "w", "E": "e", "R": "r", "T": "t","Y": "y", "U": "u", "I": "i", "O": "o", "P": "p",
                        "A": "a", "S": "s"
            , "D": "d", "F": "f", "G": "g", "H": "h", "J": "j", "K": "k", "L": "l", "Z": "z", "X": "x", "C": "c",
                        "V": "v", "B": "b"
            , "N": "n", "M": "m"}
        self.window.bind("<Return>", lambda event: self.addTheWords())
        self.window.bind("<BackSpace>", lambda event:  self.do_backspace())

        for key, letter in self.letters.items():
            self.window.bind(str(letter), lambda event, digit=key: self.combineletters(digit))
    def machinecounter(self):
            self.deltaround = self.deltaround + 1

    def deltaboxes(self, item, letter):

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




    def gameLost(self):
        self.infLabel.config(text= "The word was: " + self.randomWord, bg = "white" , fg = "red")


    def run(self):
        self.window.mainloop()





if __name__ == "__main__":
    aWordle = AdamsWordle()
    aWordle.run()
