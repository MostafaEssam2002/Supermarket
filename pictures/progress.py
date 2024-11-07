from tkinter import ttk
from tkinter import *
import tkinter as tk


def start():
          import time
          for i in range(101):
                    progress_bar["value"]=i
                    window.update_idletasks()
                    lbl1.config(text=str(i)+"%")
                    time.sleep(.05)
          progress_bar["value"]=101
window = Tk()
window.state("zoomed")
window.title("Progress Bar Example")
window.geometry("300x100")
lbl1=Label(window,font='arial 15 bold')
lbl1.pack(padx=100,pady=5)
progress_bar = ttk.Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.pack()
btn=Button(window,text="start",command=start,font='arial 15 bold',fg='navy')
btn.pack(padx=10,pady=10)
window.mainloop()
