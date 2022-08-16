import tkinter as tk
from tkinter import *
import random
import colorama



LARGE_FONT_STYLE = ("Times", 35, "bold")
DEFAULT_FONT_STYLE = ("Times", 25, "bold")

class AdamsWordle:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.minsize(375,667)
        self.window.resizable(10,10)
        self.window.title("aWordle")
        global randomWord
        randomWord = self.randomWordGenerating()
        global tempHint
        global var
        global var1
        global var2
        global var3
        global var4
        global var5
        global try1
        global try2
        global try3
        global try4
        global try5
        global wor
        global wor1
        global wor2
        global wor3
        global wor4
        global wor5

        wor = randomWord[0]
        wor1 = randomWord[1]
        wor2 = randomWord[2]
        wor3 = randomWord[3]
        wor4 = randomWord[4]


        btn = Button(self.window, text='CHECK !', bd='5',command=self.addTheWords)
        btn.place(x=37, y=150, width=300, height=40)

        hintBtn = Button(self.window, text='HINT !', bd='5', command= self.hintHelp)
        hintBtn.place(x=37, y=550, width=300, height=40)


        w = tk.Label(self.window,compound= tk.CENTER,height=2, text="ADAMS WORDLE",font=(DEFAULT_FONT_STYLE))
        w.pack()

        var = tk.StringVar()
        var2 = tk.StringVar()
        var3 = tk.StringVar()
        var4 = tk.StringVar()
        var5 = tk.StringVar()







        entry1 = tk.Entry(self.window, font=(LARGE_FONT_STYLE),justify=CENTER,textvariable=var)
        entry2 = tk.Entry(self.window, font=(LARGE_FONT_STYLE),justify=CENTER,textvariable=var2)
        entry3 = tk.Entry(self.window, font=(LARGE_FONT_STYLE),justify=CENTER,textvariable=var3)
        entry4 = tk.Entry(self.window, font=(LARGE_FONT_STYLE),justify=CENTER,textvariable=var4)
        entry5 = tk.Entry(self.window, font=(LARGE_FONT_STYLE),justify=CENTER,textvariable=var5)





        entry1.place(x=75, y=100, width=40,height=40)
        entry2.place(x=125, y=100, width=40, height=40)
        entry3.place(x=175, y=100, width=40, height=40)
        entry4.place(x=225, y=100, width=40, height=40)
        entry5.place(x=275, y=100, width=40, height=40)

        try1 = tk.Label(self.window, font=(LARGE_FONT_STYLE),bg = "White",relief = "solid")
        try2 = tk.Label(self.window, font=(LARGE_FONT_STYLE),bg = "White",relief = "solid")
        try3 = tk.Label(self.window, font=(LARGE_FONT_STYLE),bg = "White",relief = "solid")
        try4 = tk.Label(self.window, font=(LARGE_FONT_STYLE),bg = "White",relief = "solid")
        try5 = tk.Label(self.window, font=(LARGE_FONT_STYLE), bg = "White",relief = "solid")



        try1.place(x=75, y=200, width=40, height=40)
        try2.place(x=125, y=200, width=40, height=40)
        try3.place(x=175, y=200, width=40, height=40)
        try4.place(x=225, y=200, width=40, height=40)
        try5.place(x=275, y=200, width=40, height=40)

        tempHint = tk.Label(self.window, font=(LARGE_FONT_STYLE), bg="White", relief="solid")
        tempHint.place(x=37, y=600, width=300, height=40)



    def addTheWords(self):
        count = 0
        ch1 = var.get()
        ch2 = var2.get()
        ch3 = var3.get()
        ch4 = var4.get()
        ch5 = var5.get()
        words_result = (ch1, ch2, ch3, ch4, ch5)

        the_list = []
        for item in words_result:
            for word in item.split():
                the_list.append(word)

        the_list_done = "".join(the_list)

        self.newWordleCheck(the_list_done)




    def randomWordGenerating(self):
        with open(r"C:\Users\pitli\Desktop\50words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            randomWord = (random.choice(words))

            return randomWord
    def hintHelp(self):
        tempHint.config(text=randomWord)


    def newWordleCheck(self, word):
            self.wordCheck(word,randomWord)


    def wordCheck(self,list1,random):
                 if list1[0] == random[0]:
                     try1.config(text=list1[0],foreground="orange")
                 else:
                     try1.config(text=list1[0], foreground="gray")

                 if list1[1] == random[1]:
                     try2.config(text=list1[1], foreground="orange")
                 else:
                     try2.config(text=list1[1], foreground="gray")

                 if list1[2] == random[2]:
                     try3.config(text=list1[2], foreground="orange")
                 else:
                     try3.config(text=list1[2], foreground="gray")

                 if list1[3] == random[3]:
                     try4.config(text=list1[3], foreground="orange")
                 else:
                     try4.config(text=list1[3], foreground="gray")

                 if list1[4] == random[4]:
                     try5.config(text=list1[4], foreground="orange")
                 else:
                     try5.config(text=list1[4], foreground="gray")
























    def run(self):
        self.window.mainloop()




print("This is a normal text")
print(colorama.Fore.RED, "text")



if __name__ == "__main__":
    aWordle = AdamsWordle()
    aWordle.run()
"""
    def wordleCheck(self, word):
        if word == randomWord:
            try1.config(text= word)
        i in word == randomWord:
            global greenword
            greenword =
        else:
            try2.config(text=randomWord)
            try1.config(text= "wrong")
  
"""
