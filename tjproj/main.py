import tkinter as tk
import TestWiget as tw

root = tk.Tk()
root.title("Gnz")
root.geometry("250x250")

def print_wtf():
    print("wtf")

def print_happy():
    print("happy")


wiget1 = tw.TestWiget("GonzoMonk", print_wtf)
wiget1.show()
wiget2 = tw.TestWiget("GonzoMonk", print_happy)
wiget2.show()

root.mainloop()
