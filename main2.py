from tkinter import *


class Calculator:
    def __init__(self):

        #Creating main window

        self.window = Tk()
        self.window.title("Calculator")
        self.window.minsize(width=350,height=250)

        #Creating calculator UI buttons

        self.create_buttons()

        #Top small text showing the current input expression

        self.process_text = Label(text="", font=("Arial", 15, "normal"), justify="right")
        self.process_text.grid(column=0, row=1, columnspan=4, sticky="e")

        #Large result text

        self.result_text = Label(text=f"", font=("Arial", 45, "bold"), justify="right")
        self.result_text.grid(column=0, row=0, columnspan=4, sticky="e")

        #Start window loop

        self.window.mainloop()

    def create_buttons(self):
        """
        Creates all calculator buttons and places them on the grid.
        """

        buttons = [
            ("CE", self.clear, 2,0),
            ("+/-", self.toggle_sign, 2,1),
            ("%", lambda: self.button_operator("%"), 2, 2),
            ("/", lambda: self.button_operator("/"), 2, 3),

            ("7", lambda: self.button_digit("7"), 3, 0),
            ("8", lambda: self.button_digit("8"), 3, 1),
            ("9", lambda: self.button_digit("9"), 3, 2),
            ("x", lambda: self.button_operator("*"), 3, 3),

            ("4", lambda: self.button_digit("4"), 4, 0),
            ("5", lambda: self.button_digit("5"), 4, 1),
            ("6", lambda: self.button_digit("6"), 4, 2),
            ("-", lambda: self.button_operator("-"), 4, 3),

            ("1", lambda: self.button_digit("1"), 5, 0),
            ("2", lambda: self.button_digit("2"), 5, 1),
            ("3", lambda: self.button_digit("3"), 5, 2),
            ("+", lambda: self.button_operator("+"), 5, 3),

            ("0", lambda: self.button_digit("0"), 6, 0),
            (".", lambda: self.button_operator("."), 6, 2),
            ("=", self.calculate, 6, 3),
        ]

        #Create each button

        for text, command, row, column in buttons:
            #Special wide button for "0"
            if text == "0":
                button = Button(self.window,text= text, width=12,height=1,command=command,font=("Arial", 14, "bold"))
                button.grid(row= row, column= column, columnspan=2, ipadx=20, ipady=10)
            else:
                button = Button(self.window,text= text, width=1,height=1,command=command,font=("Arial", 14, "bold"))
                button.grid(row= row, column= column,  ipadx=20, ipady=10)


    def button_digit(self,digit):
        """Adds a digit to the current expression."""
        self.process_text["text"] += digit

    def button_operator(self,operator):
        """Adds an operator(+,-,*,/,etc.) to the expression."""
        self.process_text["text"] += operator

    def clear(self):
        """Clears both the input expression and result."""
        self.process_text["text"] = ""
        self.result_text["text"] = ""

    def toggle_sign(self):
        """Wraps the current expression with a negative sign."""
        current = self.process_text["text"]
        self.process_text["text"] = f"-({current})"

    def calculate(self):
        """
        Evaluates the mathematical expression using eval().
        Handles zero division and length overflow errors.
        """
        if (len(self.process_text["text"])) > 0:
            current = self.process_text["text"]
            try:
                result = eval(current)

                if result % 1 != 0:
                    self.result_text["text"] = f"{result:.2f}"
                else:
                    if len(str(result)) > 13:
                        self.result_text["text"] = "ERROR"
                        self.process_text["text"] = "ERROR"
                    else:
                        self.result_text["text"] = f"{result}"
            except ZeroDivisionError:
                self.result_text["text"] = "ERROR"
                self.process_text["text"] = "Zero Division ERROR!"


Calculator()
