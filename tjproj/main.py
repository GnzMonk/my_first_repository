import tkinter as tk
import TestWiget as tw
import TaskWidget as TaskW

root = tk.Tk()
root.title("Gnz")
root.geometry("250x250")

widget1 = TaskW.TaskWidget()
widget1.show()

widget2 = TaskW.TaskWidget(2)
widget2.show()

root.mainloop()
