import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from Bio.Seq import Seq

app = tk.Tk()
app.geometry("800x600")

app.rowconfigure((0,1),weight=1,uniform='a')
app.columnconfigure((0,1),weight=1,uniform='a')
seq = Seq('AGTTTAATCGGCGTGGATTGCCGAACCCAGGTCCTATCAGTAC')

f_one = Figure(figsize=(5,5),dpi=100)
a = f_one.add_subplot(111)
a.bar([seq.count('A'),seq.count('T'),seq.count('G'),seq.count('C')],height=1)


f_two = Figure(figsize=(5,5),dpi=100)
b = f_two.add_subplot(111)
b.pie([5,7,4,3])


f_three = Figure(figsize=(5,5),dpi=100)
c = f_three.add_subplot(111)
c.hist([seq.count('A'),seq.count('T'),seq.count('G'),seq.count('C')],bins=2)


f_four = Figure(figsize=(5,5),dpi=100)
d = f_four.add_subplot(111)
d.plot([1,2,3,4,5,6,7,8],[4,2,1,5,6,7,8,3])


canvas_one = FigureCanvasTkAgg(f_one,app)
canvas_one.draw()

canvas_two = FigureCanvasTkAgg(f_two,app)
canvas_two.draw()

canvas_three = FigureCanvasTkAgg(f_three,app)
canvas_three.draw()

canvas_four = FigureCanvasTkAgg(f_four,app)
canvas_four.draw()


canvas_one.get_tk_widget().grid(row=0,column=0,sticky=tk.NSEW)
canvas_two.get_tk_widget().grid(row=0,column=1,sticky=tk.NSEW)
canvas_three.get_tk_widget().grid(row=1,column=0,sticky=tk.NSEW)
canvas_four.get_tk_widget().grid(row=1,column=1,sticky=tk.NSEW)


app.mainloop()