import tkinter as tk

class Calculator:
    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.config(bg='#E0FFFF')

        self.wind.title('Temperature Converter')

        # Entry widget where the input and output will be shown
        self.ent = tk.Entry(self.wind, font=("Helvetica",16), justify='right', width=20)
        self.ent.insert(tk.END, '0') # Intial display on entry widget
        self.ent.grid(row=0,column=0, columnspan=4)

        # Clear button widget 
        self.btn = tk.Button(self.wind, text="Clear", font=(20),width=33, height=3, command = lambda:self.clear())
        self.btn.grid(row=1, column=0, columnspan=4)

        # Digit widgets 
        self.row = 2
        self.col = 0
        for i in "789456123":
            if self.col>2:
                self.row+=1
                self.col=0
            self.btn = tk.Button(self.wind, text=i, width=10, height=3, command=lambda d=i: self.click(d))
            self.btn.grid(row=self.row,column=self.col)
            self.col+=1
        self.btn = tk.Button(self.wind, text='0', width=10, height=3, command = lambda: self.click('0'))
        self.btn.grid(row=5,column=1)

        # Sign change Widget
        self.btn = tk.Button(self.wind, text='+/-', width=10, height=3, command = lambda: self.sign_change())
        self.btn.grid(row=4, column=0)
        
        # Opertion Widgets 
        self.row = 1
        self.col += 1
        for i in "÷x-+":
            self.btn = tk.Button(self.wind, text=i, width=10, height=3, command=lambda d=i: self.click(d))
            self.btn.grid(row=self.row,column=self.col)
            self.row+=1

        # Equal sign widget 
        self.btn = tk.Button(self.wind, text='=', width=10, height=3, command = lambda: self.result())
        self.btn.grid(row=self.row,column=self.col)

        self.ent.bind('<Key>', self.clear)

        self.wind.mainloop()

    def clear(self):
        if self.ent.get() == "0":
            self.ent.delete(0, tk.END)

    def click(self, digit):
        if self.ent.get() == ("0" or "-0"):
            self.ent.delete(0, tk.END)
        self.ent.insert(tk.END, digit)
        print(self.ent.get())

    def sign_change(self):
        self.clear
        text = self.ent.get()
        pos = self.ent.index(tk.INSERT)

        # Check if the last typed character is an arithmetic operator
        if pos > 0 and text[pos - 1] in "÷x-+":
            start = pos
            while start > 0 and text[start -1].isdigit(): # update later to include decimal sign
                start -= 1
            end = pos
            while end < len(text) and text[end].isdigit():
                end += 1

            # Change sign of number 
            if start < end:
                num = text[start:end]
                new_num = str(-float(num))
                self.ent.delete(start, end)
                self.ent.insert(start, new_num)

        else: # The last typed character is a digit so change the sign of the current number
            if text and (text[0].isdigit() or text[0] == "."):
                if text[0] == "-":
                    self.ent.delete(0, 1)
                else:
                    self.ent.insert(0, "-")

    
    def result(self):
        print(eval(self.ent.get().replace('÷','/')))


Go = Calculator()