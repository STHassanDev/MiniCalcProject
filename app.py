import tkinter as tk

class Calculator:
    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.config(bg='#E0FFFF')

        self.wind.title('Temperature Converter')

        #Entry widget where the input and output will be shown
        self.ent = tk.Entry(self.wind, font=("Helvetica",16), justify='right', width=20)
        self.ent.insert(tk.END, '0') # Intial display on entry widget
        #self.ent.pack()

        self.row = 0
        self.col = 0
        for i in "789456123":
            if self.col>2:
                self.row+=1
                self.col=0
            self.btn = tk.Button(self.wind, text=i, command=lambda d=i: self.click(d))
            self.btn.grid(row=self.row,column=self.col)
            self.col+=1


        self.ent.bind('<Key>', self.clear)

        self.wind.mainloop()

    def clear(self, event):
        if self.ent.get() == "0":
            self.ent.delete(0, tk.END)

    def click(self, digit):
        if self.ent.get() == "0":
            self.ent.delete(0, tk.END)
        self.ent.insert(tk.END, digit)
Go = Calculator()