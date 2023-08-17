import tkinter as tk

class Calculator:
    def __init__(self) -> None:
        
        self.wind = tk.Tk()

        self.wind.geometry("600x600")

        self.wind.config(bg='#E0FFFF')

        self.wind.title('Temperature Converter')

        self.wind.mainloop()

Go = Calculator()