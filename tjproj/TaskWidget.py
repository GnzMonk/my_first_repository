import tkinter as tk

class TaskWidget():
    def __init__(self, counter=1):
        self.__counter = counter
        self.__main_frame = tk.Frame(borderwidth=1, relief="solid", padx=10, pady=10)
        self.__counter_label = tk.Label(self.__main_frame, text=str(self.__counter))
        self.__task = tk.Label(self.__main_frame, text="Your task")
        self.__comment = tk.Label(self.__main_frame, text="Your comment")
        self.__task_button = tk.Button(self.__main_frame, text="red", command=self.red_task)
        self.__comment_button = tk.Button(self.__main_frame, text="red", command=self.red_comment)
        self.__del_task = tk.Button(self.__main_frame, text="complete", command=self.delete)

    def show(self):
        self.__main_frame.pack(anchor="sw")
        self.__counter_label.grid(column=0, row=0)
        self.__task.grid(column=1, row=0)
        self.__task_button.grid(column=2, row=0)
        self.__comment.grid(column=1, row=1)
        self.__comment_button.grid(column=2, row=1)
        self.__del_task.grid(column=2, row=2)

    def delete(self):
        self.__main_frame.pack_forget()
        #self.__counter_label.grid_forget()
        #self.__task.grid_forget()
        #self.__red_task.grid_forget()
        #self.__comment.grid_forget()
        #self.__red_comment.grid_forget()
        #self.__del_task.grid_forget()

    def memclear(self):
        pass

    def set_task(self, text):
        self.__task["text"] = text

    def set_comment(self, text):
        self.__comment["text"] = text

    def red_task(self):
        try:
            if self.__red_task_entry != "":
                self.set_task(self.__red_task_entry.get())
                self.__red_task_entry.destroy()
        except:
            self.__red_task_entry = tk.Entry(self.__main_frame)
            self.__red_task_entry.grid(column=1, row=0)


    def red_comment(self):
        try:
            if self.__red_comment_entry != "":
                self.set_comment(self.__red_comment_entry.get())
                self.__red_comment_entry.destroy()
        except:
            self.__red_comment_entry = tk.Entry(self.__main_frame)
            self.__red_comment_entry.grid(column=1, row=1)