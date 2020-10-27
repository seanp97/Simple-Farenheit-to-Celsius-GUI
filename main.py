from tkinter import *
import tkinter as tk

class TkinterGUI:
    def __init__(self, winTitle, xSize, ySize, *args):
         self.window = tk.Tk()
         if args:
              self.window.configure(bg=args)
         self.window.geometry(f'{xSize}x{ySize}')
         self.window.minsize(350, 150)
         self.window.title(winTitle)
         self.labelOne = Label(text="Farenheit to Celcius", font=('Helvetica 8 bold', 20))
         self.labelOne.place(x=20, y=20)
         self.entryOne = Entry(text="Enter value")
         self.entryOne.place(x=20, y=60)
         self.btnOne = Button(text="Submit", font=('Helvetica 8 bold', 15), command=self.FarenToCels)
         self.btnOne.place(x=20, y=100)
         self.resultLabel = Label(text="", font=('Helvetica 8 bold', 20))
         self.resultLabel.place(x=20, y=160)
         self.window.mainloop()

    def FarenToCels(self):
         self.getValue = self.entryOne.get()
         FarCelsEquation = float(self.getValue)
         FarCelsEquation = ((FarCelsEquation -32) * 5) / 9
         self.resultLabel.configure(text=FarCelsEquation)
    
MyNewGUI = TkinterGUI("Farenheit to Celsius GUI", 1000, 500)