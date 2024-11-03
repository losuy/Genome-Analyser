import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from collections import Counter
from Bio import SeqIO

app = tk.Tk()
app.geometry("800x600")




app.rowconfigure((0,1),weight=1,uniform='a')
app.columnconfigure((0,1),weight=1,uniform='a')
for seq_record in SeqIO.parse('D:\Programs\python\Project\gene.fna','fasta'):
    translated_1 = seq_record.seq.translate()


genome_map = Counter(seq_record.seq)
bases = list(genome_map.keys())
count = list(genome_map.values())


x = Counter(translated_1)
# del x['*']
bases_1 = list(x.keys())

count_1 = list(x.values())




f_one = Figure(figsize=(5,5),dpi=100)
a = f_one.add_subplot(111)
a.pie(genome_map.values(), labels=genome_map.keys(), autopct='%1.1f%%', startangle=90)


f_two = Figure(figsize=(5,5),dpi=100)
b = f_two.add_subplot(111)
b.bar(bases,height=count)


# f_three = Figure(figsize=(5,5),dpi=100)
# c = f_three.add_subplot(111)
# c.hist([seq.count('A'),seq.count('T'),seq.count('G'),seq.count('C')],bins=2)


f_four = Figure(figsize=(5,5),dpi=100)
d = f_four.add_subplot(111)
d.bar(bases_1,height=count_1)


canvas_one = FigureCanvasTkAgg(f_one,app)
canvas_one.draw()

canvas_two = FigureCanvasTkAgg(f_two,app)
canvas_two.draw()

# canvas_three = FigureCanvasTkAgg(f_three,app)
# canvas_three.draw()

canvas_four = FigureCanvasTkAgg(f_four,app)
canvas_four.draw()


canvas_one.get_tk_widget().grid(row=0,column=1,sticky=tk.NSEW)
canvas_two.get_tk_widget().grid(row=0,column=0,sticky=tk.NSEW)
# # canvas_three.get_tk_widget().grid(row=1,column=0,sticky=tk.NSEW)
# # canvas_one.get_tk_widget().grid(row=1,column=1,sticky=tk.NSEW)
canvas_four.get_tk_widget().grid(row=1,column=0,columnspan=2,sticky=tk.NSEW)


app.mainloop()