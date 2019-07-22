from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import xlrd
from PIL import Image, ImageTk

WIDTH = 1200
HEIGHT = 700
root = tk.Tk()
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
nb.add(page1, text='Fresh Pie')
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
        self.winfo_toplevel().title("Organization 1's Dashboard")
        self.master = master
        self.pack()
        #summer_temp_impact_score = self.get_excel_data("Input_for_Dashboard_for_MD.xlsx", 6, 2, 0)
        #summer_temp_impact_confidence = self.get_excel_data("Input_for_Dashboard_for_MD.xlsx", 6, 3, 0)
        # !!! needs to be connected to the excel sheet !!!
        self.show_image(canvas2, 'background2.jpg', 600, 350)
        self.create_graph(canvas2, 1, 0.54, 95, 266)
        self.create_graph(canvas2, -0.91, 0.11, 364, 266)
        self.create_graph(canvas2, -0.11, 0.2, 633, 266)
        self.create_graph(canvas2, -0.5, 1, 95, 455)
        self.create_graph(canvas2, 1.11, 0.2, 364, 455)
        self.create_graph(canvas2, -0.61, 0.1, 633, 455)
        self.create_graph(canvas2, -0.5, 1, 905, 81)
        self.create_graph(canvas2, 1.11, 0.2, 905, 266)
        self.create_graph(canvas2, -0.61, 0.1, 905, 455)

        canvas2.create_text(70, 612, fill="Black", font="Verdana 13", text="Organization 1", anchor="w")
        canvas2.create_text(70, 132, fill="Black", font="Verdana 40", text="54.76", anchor="sw") # add code for it to be 2 decimal points always
        canvas2.create_text(230, 132, fill="Black", font="Verdana 20", text="/100", anchor="sw")

        canvas2.create_text(195, 248, fill="Black", font="Verdana 13", text="1")
        canvas2.create_text(464, 248, fill="Black", font="Verdana 13", text="-0.91")
        canvas2.create_text(733, 248, fill="Black", font="Verdana 13", text="-0.11")

        canvas2.create_text(195, 437, fill="Black", font="Verdana 13", text="-0.5")
        canvas2.create_text(464, 437, fill="Black", font="Verdana 13", text="1.11")
        canvas2.create_text(733, 437, fill="Black", font="Verdana 13", text="-0.61")

        canvas2.create_text(1005, 63, fill="Black", font="Verdana 13", text="-0.5")
        canvas2.create_text(1005, 248, fill="Black", font="Verdana 13", text="1.11")
        canvas2.create_text(1005, 437, fill="Black", font="Verdana 13", text="-0.61")

        canvas2.create_text(183, 632, fill="Black", font="Verdana 8", text="05/12/2018", anchor="w")
        canvas2.create_text(183, 650, fill="Black", font="Verdana 8", text="16/07/2019", anchor="w")

        self.show_image(canvas1, 'background1.jpg', 600, 375)
        # [ organizational, environmental, behavioural, engagement, absenteeism, self, org-output, health]
        self.big_brain_graph(canvas1, [45,25,85,100,90,60,100,50], 50, 50)
        # [overall, presenteeism, engagement, absenteeism, self, org-output]
        self.menu_big_brain_graph(canvas1, [45,65,100,76,45,98], [45,65,100,90,45,100])  
        
    def create_graph(self, canvas, median, stdvt, x_pos, y_pos): # median: where arrow is pointing, stdvt: standard deviation
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
        colours = ['DarkOliveGreen1','DarkOliveGreen2','DarkOliveGreen3','navajo white','powder blue','slate blue','plum2','DarkOliveGreen4']
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

        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=0, extent=9*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=9*3.6, extent=14*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=23*3.6, extent=9*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=32*3.6, extent=9*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=41*3.6, extent=18*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=59*3.6, extent=18*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=77*3.6, extent=18*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_arc(x_pos,y_pos,size + x_pos,size + y_pos, start=95*3.6, extent=5*3.6, outline='darkgrey',dash=(6, 5, 2, 4), width='1.25')
        canvas.create_line(300, 300, 550, 300, fill='black', width='1.5')
        canvas.create_line(300, 300, 511.11, 166.03, fill='black', width='1.5')
        canvas.create_line(300, 300, 331.34, 51.95, fill='black', width='1.5')
        canvas.create_line(300, 300, 193.53, 73.74, fill='black', width='2.5')

        canvas.create_line(300, 300, 89.95, 164.37, fill='black', width='2.5')
        canvas.create_line(300, 300, 88.89, 433.97, fill='black', width='2.5')
        canvas.create_line(300, 300, 331.34, 548.05, fill='black', width='2.5')
        canvas.create_line(300, 300, 537.83, 377.28, fill='black', width='2.5')
 
    def menu_big_brain_graph(self, canvas, values_past, values_present):
        canvas.create_line(110,585,185,585, dash=(6, 5, 2, 4), width='1.25')
        canvas.create_line(310,585,385,585, dash=(6, 5, 2, 4), width='1.25', fill='red')
        self.show_values_overall(canvas, values_present[0], values_past[0], 600, 75)
        self.show_values_category(canvas, values_present[1], values_past[1], 900, 75)
        self.show_values_category(canvas, values_present[2], values_past[2], 600, 225)
        self.show_values_category(canvas, values_present[3], values_past[3], 900, 225)
        self.show_values_category(canvas, values_present[4], values_past[4], 600, 375)
        self.show_values_category(canvas, values_present[5], values_past[5], 900, 375)
    
    def show_values_category(self, canvas, present, past, x_pos, y_pos):
        color_circle = 'white'
        color_up = 'white'
        color_down = 'white'

        if (past != '-'):
            if (present == past):
                color_circle = 'yellow'
            elif (present > past):
                color_up = 'green'
            elif (present < past):
                color_down = 'red'
        else:
            color_circle = 'yellow'

        canvas.create_oval(x_pos + 100, y_pos + 50, x_pos + 125, y_pos + 75, fill=color_circle)
        canvas.create_polygon(x_pos + 100, y_pos + 45, x_pos + 125, y_pos + 45, x_pos + 112.5, y_pos + 25, fill=color_up, outline='black')
        canvas.create_polygon(x_pos + 100, y_pos + 80, x_pos + 125, y_pos + 80, x_pos + 112.5, y_pos + 100, fill=color_down, outline='black')
        canvas.create_text(x_pos + 56.75, y_pos + 60, fill="Black", font="Verdana 11 bold", text=past)
        #canvas.create_text(x_pos + 56.75, y_pos + 80, fill="Black", font="Verdana 8", text='past')
        canvas.create_text(x_pos + 169.25, y_pos + 60, fill="Black", font="Verdana 11 bold", text=present)
        #canvas.create_text(x_pos + 169.25, y_pos + 80, fill="Black", font="Verdana 8", text='present')
    
    def show_values_overall(self, canvas, present, past, x_pos, y_pos):
        color = 'white'
        delta = present - past
        if (present == past):
            color = 'yellow'
        elif (present > past):
            color = 'green'
        elif (present < past):
            color = 'red'
            
        canvas.create_text(x_pos + 56.75, y_pos + 60, fill="Black", font="Verdana 18 bold", text=past)
        #canvas.create_text(x_pos + 56.75, y_pos + 80, fill="Black", font="Verdana 8", text='total')
        canvas.create_text(x_pos + 169.25, y_pos + 60, fill=color, font="Verdana 18 bold", text=delta)
        #canvas.create_text(x_pos + 169.25, y_pos + 80, fill="Black", font="Verdana 8", text='delta')

    def show_image(self, canvas, filename, x, y):
        img = Image.open(filename)
        canvas.image = ImageTk.PhotoImage(img)
        canvas.create_image(x, y, image=canvas.image)

    def find_rgb(self, colour):
        rgb = canvas1.winfo_rgb(colour)
        red, green, blue = rgb[0]/256, rgb[1]/256, rgb[2]/256
        print("R: %d, G: %d, B: %d" %(red, green, blue))

app = Application(master=root)
app.mainloop()