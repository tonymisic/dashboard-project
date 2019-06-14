from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import xlrd

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.winfo_toplevel().title("Dashboard")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

#drawing
root = tk.Tk()

#tabs
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
text = ScrolledText(page2)
text.pack(expand=1, fill="both")
nb.add(page1, text='Dashboard 1')
nb.add(page2, text='Dashboard 2')
nb.add(page3, text='Dashboard 3')
nb.add(page4, text='Dashboard 4')
nb.pack(expand=1, fill="both")

canvas = tk.Canvas(page1, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_arc(50, 50, 200, 200, start=0, extent=180)

#excel connection
workbook = xlrd.open_workbook('data.xlsx')
sheet = workbook.sheet_by_index(0)
if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    print("Empty Cell")
else:
    print(sheet.cell(0, 0).value)

app = Application(master=root)
app.mainloop()