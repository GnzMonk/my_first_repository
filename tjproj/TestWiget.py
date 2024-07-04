import tkinter as tk

class TestWiget:
    def __init__(self, text, button_function):
        self.__main_frame = tk.Frame(borderwidth=1, relief="solid", padx=10, pady=10)
        self.__text = text
        self.__text_wiget = tk.Label(self.__main_frame, text=self.__text)
        self.__func_button = button_function
        self.__run_button = tk.Button(self.__main_frame, text="run", command=self.__func_button)
        self.___result_text = tk.Label(self.__main_frame, text='result')


    def show(self):
        try:
            self.__text_wiget.pack(anchor="w")
            self.__run_button.pack(anchor="w")
            self.__main_frame.pack(fill="x")
            self.___result_text.pack()
        except:
            print("Object wasn't found")

    def delete(self):
        self.__run_button.pack_forget()
        self.__text_wiget.pack_forget()
        self.__main_frame.pack_forget()
        self.___result_text.pack_forget()

    def memclear(self):
        self.__run_button.destroy()
        self.__text_wiget.destroy()
        self.__main_frame.destroy()
        self.___result_text.destroy()

    def set_result(self, text):
        self.___result_text["text"] = text