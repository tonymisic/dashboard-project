from tkinter import ttk
import tkinter as tk
import xlrd
from PIL import Image, ImageTk
from datetime import datetime

WIDTH = 1200
HEIGHT = 700
root = tk.Tk()
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
nb.add(page1, text='Overall')
nb.add(page2, text='Environmental')
nb.add(page3, text='Organization')
nb.add(page4, text='Engagement')
nb.pack(expand=1, fill="both")
canvas1 = tk.Canvas(page1, width=WIDTH, height=HEIGHT)
canvas1.pack(fill="both", expand=True)
canvas2 = tk.Canvas(page2, width=WIDTH, height=HEIGHT)
canvas2.pack(fill="both", expand=True)
canvas3 = tk.Canvas(page3, width=WIDTH, height=HEIGHT)
canvas3.pack(fill="both", expand=True)
canvas4 = tk.Canvas(page4, width=WIDTH, height=HEIGHT)
canvas4.pack(fill="both", expand=True)

def scaleBetween(unscaledNum):
    return round(((4 * unscaledNum) / (100)) - 2, 2)

# excel sheet
workbook = xlrd.open_workbook("Input_for_Dashboard_for_MD.xlsx")
sheet = workbook.sheet_by_index(0)

# previous information, orgname, dates.
organizationName = sheet.cell(5, 11).value
pdc = int(sheet.cell(8, 11).value)
dt = str(datetime.fromordinal(datetime(1900, 1, 1).toordinal() + pdc - 2))
now = str(datetime.now())
currentDate = now[8:10]+ "/" + now[5:7] + "/" + now[0:4]
previousDateOfCompletion = dt[8:10] + "/" + dt[5:7] + "/" + dt[0:4]
previousOverallScore = float(sheet.cell(11, 11).value)
previousEngagement = float(sheet.cell(14, 11).value)
previousPresenteeism = float(sheet.cell(17, 11).value)
previousAbsenteeism = float(sheet.cell(20, 11).value)
previousSelfAssessment = float(sheet.cell(23, 11).value)
previousOrgOutput = float(sheet.cell(26, 11).value)

# variables
presenteeism = round(float(sheet.cell(4,2).value), 2)
engagement = round(float(sheet.cell(32,2).value), 2)
absenteeism = round(float(sheet.cell(48,2).value), 2)
selfAssessment = round(float(sheet.cell(45,2).value), 2)
orgOutput = round(float(sheet.cell(49,2).value), 2)
organizational = round(float(sheet.cell(26,2).value), 2)
environmental = round(float(sheet.cell(5,2).value), 2)
behavioural = round(float(sheet.cell(30,2).value), 2)
health = round(float(sheet.cell(31,2).value), 2)
overallScore = round(float(45), 2) ## To Do

behaviouralConfidence = round(float(sheet.cell(30,3).value), 2)
healthConfidence = round(float(sheet.cell(31,3).value), 2)

# environment
tempImpactSummerScore = round(float(sheet.cell(6,2).value), 2)
tempImpactWinterScore = round(float(sheet.cell(7,2).value), 2)
tempImpactSpringScore = round(float(sheet.cell(8,2).value), 2)
tempImpactFallScore = round(float(sheet.cell(9,2).value), 2)

tempCondSummerScore = round(float(sheet.cell(10,2).value), 2)
tempCondWinterScore = round(float(sheet.cell(11,2).value), 2)
tempCondSpringScore = round(float(sheet.cell(12,2).value), 2)
tempCondFallScore = round(float(sheet.cell(13,2).value), 2)

humidityImpactSummer = round(float(sheet.cell(14,2).value), 2)
humidityImpactWinter = round(float(sheet.cell(15,2).value), 2)
humidityImpactSpring = round(float(sheet.cell(16,2).value), 2)
humidityImpactFall =  round(float(sheet.cell(17,2).value), 2)

humidityCondSummer = round(float(sheet.cell(18,2).value), 2)
humidityCondWinter = round(float(sheet.cell(19,2).value), 2)
humidityCondSpring = round(float(sheet.cell(20,2).value), 2)
humidityCondFall = round(float(sheet.cell(21,2).value), 2)

noiseImpact = round(float(sheet.cell(22,2).value), 2)
noiseCondition = round(float(sheet.cell(23,2).value), 2) 
artificialLightImpact = round(float(sheet.cell(24,2).value), 2) 
artificialLightCondition = round(float(sheet.cell(25,2).value), 2) 
naturalLightImpact = round(float(sheet.cell(24,2).value), 2) 
naturalLightCondition = round(float(sheet.cell(25,2).value), 2) # no value in excel, currently a duplicate

tempCondSummerConfidence = round(float(sheet.cell(10,3).value), 2)

# engagement canvas 4
overallVigor = round(float(sheet.cell(33,2).value), 2)
excitement = round(float(sheet.cell(34,2).value), 2)
perseverence = round(float(sheet.cell(35,2).value), 2)
endurance = round(float(sheet.cell(36,2).value), 2)
overallDedication = round(float(sheet.cell(37,2).value), 2)
pride = round(float(sheet.cell(38,2).value), 2)
enthusiasm = round(float(sheet.cell(39,2).value), 2)
inspiration = round(float(sheet.cell(40,2).value), 2)
overallAbsorption = round(float(sheet.cell(41,2).value), 2)
attachment = round(float(sheet.cell(42,2).value), 2)
absorption = round(float(sheet.cell(43,2).value), 2)
immersion = round(float(sheet.cell(44,2).value), 2)

qualityOfWorkScore = round(float(sheet.cell(46,2).value), 2)
qualityOfWorkConfidence = round(float(sheet.cell(46,3).value), 2)
volumeOfWorkScore = round(float(sheet.cell(47,2).value), 2)
volumeOfWorkConfidence = round(float(sheet.cell(47,3).value), 2)

seperationScore = scaleBetween(round(float(sheet.cell(27,2).value), 2))
seperationConfidence = round(float(sheet.cell(27,3).value), 2)
hierarchyScore = scaleBetween(round(float(sheet.cell(28,2).value), 2))
hierarchyConfidence = round(float(sheet.cell(28,3).value), 2)
directionScore = scaleBetween(round(float(sheet.cell(29,2).value), 2))
directionConfidence = round(float(sheet.cell(29,3).value), 2)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        title = organizationName + "'s Dashboard"
        self.winfo_toplevel().title(title)
        self.master = master
        self.pack()
        
        # canvas 2
        self.show_image(canvas2, 'background2.jpg', 600, 350)
        self.create_graph(canvas2, tempCondSummerScore, tempCondSummerConfidence, 95, 266)
        self.create_graph(canvas2, -0.91, 0.11, 364, 266)
        self.create_graph(canvas2, -0.11, 0.2, 633, 266)
        self.create_graph(canvas2, -0.5, 1, 95, 455)
        self.create_graph(canvas2, 1.11, 0.2, 364, 455)
        self.create_graph(canvas2, -0.61, 0.1, 633, 455)
        self.create_graph(canvas2, -0.5, 1, 905, 81)
        self.create_graph(canvas2, 1.11, 0.2, 905, 266)
        self.create_graph(canvas2, -0.61, 0.1, 905, 455)

        canvas2.create_text(70, 612, fill="Black", font="Verdana 13", text=organizationName, anchor="w")
        canvas2.create_text(70, 132, fill="Black", font="Verdana 40", text=environmental, anchor="sw")
        canvas2.create_text(230, 132, fill="Black", font="Verdana 20", text="/100", anchor="sw")

        canvas2.create_text(195, 248, fill="Black", font="Verdana 13", text=humidityImpactSummer) # might need to be labeled better
        canvas2.create_text(464, 248, fill="Black", font="Verdana 13", text=humidityImpactWinter)
        canvas2.create_text(733, 248, fill="Black", font="Verdana 13", text=humidityImpactSpring) # might need to average

        canvas2.create_text(195, 437, fill="Black", font="Verdana 13", text=tempImpactSummerScore)
        canvas2.create_text(464, 437, fill="Black", font="Verdana 13", text=tempImpactWinterScore)
        canvas2.create_text(733, 437, fill="Black", font="Verdana 13", text=tempImpactSpringScore)

        canvas2.create_text(1005, 63, fill="Black", font="Verdana 13", text=noiseImpact)
        canvas2.create_text(1005, 248, fill="Black", font="Verdana 13", text=artificialLightImpact)
        canvas2.create_text(1005, 437, fill="Black", font="Verdana 13", text=naturalLightImpact)

        canvas2.create_text(183, 632, fill="Black", font="Verdana 8", text=previousDateOfCompletion, anchor="w")
        canvas2.create_text(183, 650, fill="Black", font="Verdana 8", text=currentDate, anchor="w")

        # canvas 1 DONE
        self.show_image(canvas1, 'background1.jpg', 600, 375)
        # [ organizational, environmental, behavioural, engagement, absenteeism, self, org-output, health]
        self.big_brain_graph(canvas1, [organizational,environmental,behavioural,engagement,absenteeism,selfAssessment,orgOutput,health], 50, 50)
        # [overall, presenteeism, engagement, absenteeism, self, org-output]
        self.menu_big_brain_graph(canvas1, [previousOverallScore,previousPresenteeism,previousEngagement,previousAbsenteeism,previousSelfAssessment,previousOrgOutput], [overallScore,presenteeism,engagement,absenteeism,selfAssessment,orgOutput])
        canvas1.create_text(60, 622, fill="Black", font="Verdana 13", text=organizationName, anchor="w")
        canvas1.create_text(180, 640, fill="Black", font="Verdana 8", text=previousDateOfCompletion, anchor="w")
        canvas1.create_text(180, 659, fill="Black", font="Verdana 8", text=currentDate, anchor="w")
        
        #canvas 3
        self.show_image(canvas3, 'background3.jpg', 600, 350)

        canvas3.create_text(70, 85, fill="Black", font="Verdana 18 bold", text=organizational, anchor="w")
        canvas3.create_text(160, 91, fill="Black", font="Verdana 15 bold", text="/100", anchor="w")
        canvas3.create_text(611, 85, fill="Black", font="Verdana 18 bold", text=behavioural, anchor="w")
        canvas3.create_text(701, 91, fill="Black", font="Verdana 15 bold", text="/100", anchor="w")
        canvas3.create_text(880, 85, fill="Black", font="Verdana 18 bold", text=health, anchor="w")
        canvas3.create_text(970, 91, fill="Black", font="Verdana 15 bold", text="/100", anchor="w")

        self.create_graph(canvas3, seperationScore, seperationConfidence, 106, 190)
        self.create_graph(canvas3, directionScore, directionConfidence, 106, 398)
        self.create_graph(canvas3, hierarchyScore, hierarchyConfidence, 351, 190)
        self.create_graph(canvas3, -0.61, 0.1, 351, 398) # not sure if we need this
        self.create_graph(canvas3, scaleBetween(behavioural), behaviouralConfidence, 633, 190)
        self.create_graph(canvas3, scaleBetween(health), healthConfidence, 905, 190)
        
        canvas3.create_text(206, 172, fill="Black", font="Verdana 13", text="1.08") # need to get rid of these
        canvas3.create_text(206, 379, fill="Black", font="Verdana 13", text="-0.91")
        canvas3.create_text(455, 172, fill="Black", font="Verdana 13", text="-0.11")
        canvas3.create_text(455, 379, fill="Black", font="Verdana 13", text="-0.52")
        canvas3.create_text(70, 612, fill="Black", font="Verdana 13", text=organizationName, anchor="w")
        canvas3.create_text(183, 632, fill="Black", font="Verdana 8", text=previousDateOfCompletion, anchor="w")
        canvas3.create_text(183, 650, fill="Black", font="Verdana 8", text=currentDate, anchor="w")

        #canvas 4
        self.show_image(canvas4, 'background4.jpg', 600, 350)
        canvas4.create_text(70, 71, fill="Black", font="Verdana 15 bold", text=engagement, anchor="w")
        canvas4.create_text(140, 77, fill="Black", font="Verdana 13 bold", text="/100", anchor="w")
        canvas4.create_text(611, 71, fill="Black", font="Verdana 15 bold", text=selfAssessment, anchor="w")
        canvas4.create_text(681, 77, fill="Black", font="Verdana 13 bold", text="/100", anchor="w")
        canvas4.create_text(880, 71, fill="Black", font="Verdana 15 bold", text=absenteeism, anchor="w")
        canvas4.create_text(951, 77, fill="Black", font="Verdana 13 bold", text="/100", anchor="w")
        canvas4.create_text(880, 352, fill="Black", font="Verdana 15 bold", text=orgOutput, anchor="w")
        canvas4.create_text(951, 358, fill="Black", font="Verdana 13 bold", text="/100", anchor="w")

        canvas4.create_text(150, 175, fill="Black", font="Verdana 19 bold", text=overallVigor)
        canvas4.create_text(329, 175, fill="Black", font="Verdana 19 bold", text=overallAbsorption)
        canvas4.create_text(505, 175, fill="Black", font="Verdana 19 bold", text=overallDedication)

        canvas4.create_text(150, 307, fill="Black", font="Verdana 19", text=excitement)
        canvas4.create_text(150, 422, fill="Black", font="Verdana 19", text=perseverence)
        canvas4.create_text(150, 536, fill="Black", font="Verdana 19", text=endurance)
        
        canvas4.create_text(329, 307, fill="Black", font="Verdana 19", text=pride)
        canvas4.create_text(329, 422, fill="Black", font="Verdana 19", text=enthusiasm)
        canvas4.create_text(329, 536, fill="Black", font="Verdana 19", text=inspiration)
        
        canvas4.create_text(505, 305, fill="Black", font="Verdana 19", text=attachment)
        canvas4.create_text(505, 422, fill="Black", font="Verdana 19", text=absorption)
        canvas4.create_text(505, 536, fill="Black", font="Verdana 19", text=immersion)

        self.create_graph(canvas4, qualityOfWorkScore, qualityOfWorkConfidence, 633, 168)
        self.create_graph(canvas4, volumeOfWorkScore, volumeOfWorkConfidence, 633, 346)
        self.create_graph(canvas4, 1.11, 0.2, 905, 103)
        self.create_graph(canvas4, -0.61, 0.1, 905, 384)

        canvas4.create_text(70, 612, fill="Black", font="Verdana 13", text=organizationName, anchor="w")
        canvas4.create_text(183, 632, fill="Black", font="Verdana 8", text=previousDateOfCompletion, anchor="w")
        canvas4.create_text(183, 650, fill="Black", font="Verdana 8", text=currentDate, anchor="w")
        
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
        canvas.create_text(x_pos + 169.25, y_pos + 60, fill=color, font="Verdana 18 bold", text=round(delta, 2))
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