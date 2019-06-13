import tkinter as tk
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

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300)
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