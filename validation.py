##Validation Library
from tkinter import *
from tkinter.messagebox import*
def ValidPrice(entry):
    priceStr= entry.get
    price=float(priceStr)
    if price <0:
        valid = False
    else:
        valid= True
    if not valid:
        showerror("ERROR","Must be a value greater than or equal to zero!")
        entry.delete(0,END)
        entry.focus_set()
def ValidCalcalulation(entry):
    Number= entry.get()
    valid = True
    for no in Number:
        if not (no in "0123456789"):
            valid = False
            errormessage = "That is not an integer, please enter an integer"
        
    if Number == "":
        valid = False
        errormessage = "You have typed nothing in, please enter an answer"
    if not valid:
        showerror("Error",errormessage)
        entry.delete(0,END)
        entry.focus_set()
def ValidSave(entry):
    Number = entry
    valid = True
    if Number < 10:
        valid = False
        errormessage = "To save please answer a minimum of 10 Questions."
    if not valid:
        showerror("Error",errormessage)
        
        
