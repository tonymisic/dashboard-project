from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import xlrd

WIDTH = 1200
HEIGHT = 600
root = tk.Tk()
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
nb.add(page1, text='Dashboard 1')
nb.add(page2, text='Environmental')
nb.add(page3, text='Dashboard 3')
nb.add(page4, text='Dashboard 4')
nb.pack(expand=1, fill="both")
canvas1 = tk.Canvas(page1, width=WIDTH, height=HEIGHT)
canvas1.pack(fill="both", expand=True)
canvas2 = tk.Canvas(page2, width=WIDTH, height=HEIGHT)
canvas2.pack(fill="both", expand=True)
canvas3 = tk.Canvas(page3, width=WIDTH, height=HEIGHT)
canvas3.pack(fill="both", expand=True)
canvas4 = tk.Canvas(page4, width=WIDTH, height=HEIGHT)
canvas4.pack(fill="both", expand=True)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.winfo_toplevel().title("IBI Dashboard")
        self.master = master
        self.pack()
        #summer_temp_impact_score = self.get_excel_data("Input_for_Dashboard_for_MD.xlsx", 6, 2, 0)
        #summer_temp_impact_confidence = self.get_excel_data("Input_for_Dashboard_for_MD.xlsx", 6, 3, 0)
        self.create_graph(canvas2, 0.13, 0.11, 100, 100, "-2 Far Too Dry", "+2 Far Too Humid")
        self.create_graph(canvas2, -0.91, 0.11, 500, 100, "-2 Far Too Dry", "+2 Far Too Humid")
        self.create_graph(canvas2, -0.11, 0.2, 900, 100, "-2 Far Too Dry", "+2 Far Too Humid")
        self.create_graph(canvas2, -0.5, 1, 100, 400, "-2 Far Too Dry", "+2 Far Too Humid")
        self.create_graph(canvas2, 1.11, 0.2, 500, 400, "-2 Far Too Dry", "+2 Far Too Humid")
        self.create_graph(canvas2, -0.61, 0.1, 900, 400, "-2 Far Too Dry", "+2 Far Too Humid")

        self.big_brain_graph(canvas1, [45,25,85,100,90,60,30,50], 50, 50)
        self.menu_big_brain_graph(canvas1)

    def create_graph(self, canvas, median, stdvt, x_pos, y_pos, text_min, text_max): # median: where arrow is pointing, stdvt: standard deviation
        size = 200
        text_offset = 110
        confidence = stdvt * 45
        mid_point = 90
        if (median == 0):
            mid_point = 90
        elif (median > 0):
            mid_point = 90 - (median * 45)
        elif (median < 0):
            mid_point = (abs(median) * 45) + 90

        canvas.create_arc(x_pos, y_pos, size + x_pos, size + y_pos, start=mid_point - confidence/2, extent=confidence,outline='lightgrey', fill='lightgrey') # standard deviation
        canvas.create_arc(x_pos, y_pos, size + x_pos, size + y_pos, start=mid_point, extent=0, fill='blue') # median
        canvas.create_arc(x_pos, y_pos, size + x_pos, size + y_pos, start=0, extent=180) # full graph
        canvas.create_text(x_pos, y_pos + text_offset,fill="black",font="Times 10 bold", text=text_min)
        canvas.create_text(x_pos + size, y_pos + text_offset,fill="black",font="Times 10 bold", text=text_max)

    def get_excel_data(self, filename, row, col, sheet_num):
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(sheet_num)
        if sheet.cell(row, col).value == xlrd.empty_cell.value:
            print("Empty Cell")
        else:
            return sheet.cell(row, col).value

    def big_brain_graph(self, canvas, values, x_pos, y_pos): # values is a list of 8
        size = 500
        original_x = x_pos
        original_y = y_pos
        starts = [0,9,23,32,41,59,77,95]
        extents = [9,14,9,9,18,18,18,5]
        colours = ['darkgreen','green','lightgreen','orange','lightblue','purple','lightgrey','grey']
        for i in range(8): # value might change if graph is moved
            x = (((values[i] - 0) * (50 - 300)) / (100 - 0)) + 300
            y = (((values[i] - 0) * (50 - 300)) / (100 - 0)) + 300
            s = values[i]/100 * 500
            canvas.create_arc(x, y, s + x, s + y, start=starts[i]*3.6, extent=extents[i]*3.6,fill=colours[i], outline='')

        color = 'gray'
        for i in range(9):
            if i == 4:
                color = 'red'
            else:
                color = 'darkgrey'
            x_pos = x_pos + 25
            y_pos = y_pos + 25
            size = size - 50
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=0, extent=9*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=9*3.6, extent=14*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=23*3.6, extent=9*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=32*3.6, extent=9*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=41*3.6, extent=18*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=59*3.6, extent=18*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=77*3.6, extent=18*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
            canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=95*3.6, extent=5*3.6, outline=color,dash=(6, 5, 2, 4), width='1.25')
        
        x_pos = original_x
        y_pos = original_y
        size = 500

        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=0, extent=9*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=9*3.6, extent=14*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=23*3.6, extent=9*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=32*3.6, extent=9*3.6, outline='black', width='2')
        
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=41*3.6, extent=18*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=59*3.6, extent=18*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=77*3.6, extent=18*3.6, outline='black', width='2')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=95*3.6, extent=5*3.6, outline='black', width='2')
 
    def menu_big_brain_graph(self, canvas):
        canvas.create_rectangle(600, 50, 825, 75, fill='lightgrey')
        canvas.create_text(712.5, 62.5,fill="Black",font="Verdana 11 bold", text='Overall Scoring')
        canvas.create_rectangle(900, 50, 1125, 75, fill='lightgreen')
        canvas.create_text(1012.5, 62.5,fill="Black",font="Verdana 11 bold", text='Presenteeism')
        canvas.create_rectangle(600, 200, 825, 225, fill='orange')
        canvas.create_text(712.5, 212.5,fill="Black",font="Verdana 11 bold", text='Engagement')
        canvas.create_rectangle(900, 200, 1125, 225, fill='lightblue')
        canvas.create_text(1012.5, 212.5,fill="Black",font="Verdana 11 bold", text='Absenteeism')
        canvas.create_rectangle(600, 350, 825, 375, fill='purple')
        canvas.create_text(712.5, 362.5,fill="White",font="Verdana 11 bold", text='Self-Assessment')
        canvas.create_rectangle(900, 350, 1125, 375, fill='lightyellow')
        canvas.create_text(1012.5, 362.5,fill="Black",font="Verdana 11 bold", text='Organizational Outputs')

        canvas.create_rectangle(600, 500, 1125, 525, fill='lightgrey')
    
    def show_values_category(self, canvas, present, past, x_pos, y_pos):
        

app = Application(master=root)
app.mainloop()
