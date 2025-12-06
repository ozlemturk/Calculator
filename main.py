from tkinter import *

#-------------UI-------------#
class Calculator():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.minsize(width=350,height=250)
        self.buton()
        self.islem_text = Label(text="", font=("Arial", 15, "normal"), justify="right")
        self.islem_text.grid(column=0, row=1, columnspan=4, sticky="e")
        self.sonuc_text = Label(text=f"", font=("Arial", 45, "bold"), justify="right")
        self.sonuc_text.grid(column=0, row=0, columnspan=4, sticky="e")
        self.window.mainloop()  # <-- burada çağrılmalı

    def buton(self):
        #CE Button
        buton1 = Button(self.window, text="CE",width=1, height=1, font=("Arial", 14,"bold"),command = self.buton_islem_ce)
        buton1.grid(column=0, row=2, ipadx=20, ipady=10)
        #+/- Button
        buton2 = Button(self.window, text="+/-",width=1, height=1, font=("Arial", 14,"bold"),command=self.buton_islem_abs)
        buton2.grid(column=1, row=2, ipadx=20, ipady=10)
        #% Button
        buton3 = Button(self.window, text="%",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_yuzde)
        buton3.grid(column=2, row=2, ipadx=20, ipady=10)
        #/ Button
        buton4 = Button(self.window, text="/",width=1, height=1, font=("Arial", 14,"bold"),command=self.buton_islem_bolme)
        buton4.grid(column=3, row=2, ipadx=20, ipady=10)
        #7 Button
        buton5 = Button(self.window, text="7",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_7)
        buton5.grid(column=0, row=3, ipadx=20, ipady=10)
        #8 Button
        buton6 = Button(self.window, text="8",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_8)
        buton6.grid(column=1, row=3, ipadx=20, ipady=10)
        #9 Button
        buton7 = Button(self.window, text="9",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_9)
        buton7.grid(column=2, row=3, ipadx=20, ipady=10)
        #x Button
        buton8 = Button(self.window, text="x",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_carpma)
        buton8.grid(column=3, row=3, ipadx=20, ipady=10)
        #4 Button
        buton9 = Button(self.window, text="4",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_4)
        buton9.grid(column=0, row=4, ipadx=20, ipady=10)
        #5 Button
        buton10 = Button(self.window, text="5",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_5)
        buton10.grid(column=1, row=4, ipadx=20, ipady=10)
        #6 Button
        buton11 = Button(self.window, text="6",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_6)
        buton11.grid(column=2, row=4, ipadx=20, ipady=10)
        #- Button
        buton12 = Button(self.window, text="-",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_cikarma)
        buton12.grid(column=3, row=4, ipadx=20, ipady=10)
        #1 Button
        buton13 = Button(self.window, text="1",width=1, height=1, font=("Arial", 14,"bold"),command=self.buton_islem_1)
        buton13.grid(column=0, row=5, ipadx=20, ipady=10)
        #2 Button
        buton14 = Button(self.window, text="2",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_2)
        buton14.grid(column=1, row=5, ipadx=20, ipady=10)
        #3 Button
        buton15 = Button(self.window, text="3",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_3)
        buton15.grid(column=2, row=5, ipadx=20, ipady=10)
        #+ Button
        buton16 = Button(self.window, text="+",width=1, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_toplama)
        buton16.grid(column=3, row=5, ipadx=20, ipady=10)
        #0 Button
        buton17= Button(self.window, text="0",width=12, height=1, font=("Arial", 14,"bold"), command=self.buton_islem_0)
        buton17.grid(column=0, row=6,columnspan=2, ipadx=20, ipady=10)
        #. Button
        buton18 = Button(self.window, text=".",width=1, height=1, font=("Arial", 14,"bold"),command=self.buton_islem_nokta)
        buton18.grid(column=2, row=6,ipadx=20, ipady=10)
        #= Button
        buton19 = Button(self.window, text="=",width=1, height=1, font=("Arial", 14,"bold"),command=self.sonuc)
        buton19.grid(column=3, row=6, ipadx=20, ipady=10)

    def buton_islem_1(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "1"

    def buton_islem_2(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "2"

    def buton_islem_3(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "3"

    def buton_islem_4(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "4"

    def buton_islem_5(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "5"

    def buton_islem_6(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "6"

    def buton_islem_7(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "7"

    def buton_islem_8(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "8"

    def buton_islem_9(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "9"

    def buton_islem_0(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "0"

    def buton_islem_yuzde(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "%"

    def buton_islem_bolme(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "/"

    def buton_islem_carpma(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "*"

    def buton_islem_cikarma(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "-"

    def buton_islem_toplama(self):
        current =self.islem_text["text"]
        self.islem_text["text"] = current + "+"

    def buton_islem_ce(self):
        self.islem_text["text"] = ""
        self.sonuc_text["text"] = ""

    def buton_islem_nokta(self):
        current = self.islem_text["text"]
        self.islem_text["text"] = current + "."

    def buton_islem_abs(self):
        current = self.islem_text["text"]
        self.islem_text["text"] = f"-({current})"





    def sonuc(self):
        if len(self.islem_text["text"]) > 0:
            current = self.islem_text["text"]
            try:
                result = eval(current)
                if result % 1 != 0:
                    self.sonuc_text["text"] = f"{result:.2f}"
                else:
                    if len(str(result)) > 13:
                        self.islem_text["text"] = "ERROR"
                        self.sonuc_text["text"] = "ERROR"
                    else:
                        self.sonuc_text["text"] = f"{result}"
            except ZeroDivisionError:
                self.sonuc_text["text"] = "ERROR"
                self.islem_text["text"] = "Zero Division ERROR!"


Calculator()
