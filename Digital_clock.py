# first import time, secondly import tkinter
from time import strftime
from tkinter import Label, Tk

# Creating the window for the clock
window = Tk()
window.title("CLOCK")
window.geometry("200x80")
window.configure(bg="black")
window.resizable(False, False)
# creating the label function

clock_label = Label(window, bg="black", fg="yellow", font=("Times", 30, 'bold'), relief='flat')
clock_label.place(x=20, y=30)


def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(80, updating_label)#the clock updates every 80 millisecond


# Calling the update label function
updating_label()

# The loop that makes our window stable
window.mainloop()
