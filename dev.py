import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        menu=tk.Menu(self.master)
        self.master.config(menu)
        file = tk.Menu(menu)
        file.add_comand(label='Exit', command=theeixt)
    def theeixt(self):
        exit
# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)


# start the program
myapp.mainloop()