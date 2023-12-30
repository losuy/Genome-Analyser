import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Bio.Seq import Seq
import customtkinter as CTk

class App(tk.Tk):
    def __init__(self,title,size):
        super().__init__()

        self.geometry(f"{size[0]}x{size[1]}")

        self.title(title)
        self.resizable(0,0)
        self.app_frame = App_frame(self)
        self.main = Main(self.app_frame)
        self.menu = Menu(self.app_frame,self.main)

        self.mainloop()


class App_frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.image = tk.PhotoImage(file='project/images/Untitled_design.png')
        self.label = tk.Label(self,image=self.image)
        self.label.place(x=0,y=0)

        self.place(x=0,y=0,relwidth=1,relheight=1)


class Menu(tk.Frame):
    def __init__(self,parent,main):
        super().__init__(parent)

        self.main = main
        self.create_widget()
        self.place(x=10,y=10,relwidth=0.3,relheight=0.97)

    def create_widget(self):
       button_1 = tk.Button(self,text = 'button 1',
       command = lambda: self.main.show_frame(page_name ='PageOne'))
       button_2 = tk.Button(self,text = 'button 2',
       command = lambda: self.main.show_frame(page_name ='PageTwo'))
       button_3 = tk.Button(self,text = 'button 3',
       command = lambda:self. main.show_frame(page_name ='PageThree'))
       button_4 = tk.Button(self,text = 'button 4',
       command = lambda: self.main.show_frame(page_name ='PageFour'))
       button_5 = tk.Button(self,text = 'button 5',
       command = lambda: self.main.show_frame(page_name ='PageFive'))
       
       page_name =self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
       self.columnconfigure(0,weight=1,uniform='a')

       button_1.grid(row=0,column=0,sticky='nsew')
       button_2.grid(row=1,column=0,sticky='nsew')
       button_3.grid(row=2,column=0,sticky='nsew')
       button_4.grid(row=3,column=0,sticky='nsew')
       button_5.grid(row=4,column=0,sticky='nsew')


class Main(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        # tk.Label(self,background='white').pack(fill='both',expand=True)
        self.frames = (PageFive,PageFour,PageThree,PageTwo,PageOne)
        self.pages = {}

        print(self.create_and_map_pages())
        self.place(x=0,relx=0.34,y=10,relwidth=0.65,relheight=0.97)
 

    def create_and_map_pages(self):
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
        for F in self.frames:
            frames = F(self)
            self.pages[str(F.__name__)] = frames
            frames.grid(row=0,column=0,sticky="nsew")

        return self.pages

    def show_frame(self,page_name):
        frame = self.pages[page_name]
        frame.tkraise()



class PageOne(tk.Frame):

    OPTIONS = ['compliment','reverse compliment','transcribe','translate'] 

    def __init__(self,parent):
        super().__init__(parent)

        self.main_frame = tk.Frame(self,bg='red')
        self.widget_frame = tk.Frame(self.main_frame,bg='yellow')
        self.check_frame = tk.Frame(self.main_frame,bg='blue')


        self.temporary_list = self.create_check_boxes()
        self.Buttons()
        self.entries = self.Entries()
        self.pack_frames()


    def pack_frames(self):
        self.main_frame.pack(fill='both',expand=True)
        self.widget_frame.place(rely=0.1,relheight=0.2,relwidth=1)
        self.check_frame.place(rely=0.3,relheight=0.4,relwidth=1)

    def Buttons(self):
        button = tk.Button(self.widget_frame,text='PRESS',command=self.validate_dna_sequence)
        options_validate_button = tk.Button(self.check_frame,text='PRESS',command=self.
                                            validate_dna_sequence)
        
        options_validate_button.pack(side=tk.TOP,padx=10,anchor=tk.W,expand=True)
        
        button.pack(side='right',fill='both',expand=True)   

    def Entries(self):
        entry = tk.Entry(self.widget_frame,textvariable='')
        entry.pack(side='left',expand=True,fill='both')
        return entry


    def create_check_boxes(self):
        temporary_list = [tk.StringVar(value='') for i in  self.OPTIONS]
        # check_frame.rowconfigure([0,1,2,3,4],weight=1,uniform='a')
        self.check_frame.columnconfigure([0],weight=1,uniform='a')
        self.check_frame.rowconfigure([1],weight=1,uniform='a')

        for i in range(0,len( self.OPTIONS)):
            frame = tk.Checkbutton(self.check_frame,text= self.OPTIONS[i],variable=temporary_list[i],
                               onvalue= self.OPTIONS[i],offvalue='')
            frame.pack(side=tk.TOP,anchor=tk.W,padx=10,expand=True)

        return temporary_list 
    
    
    def procedure(self,sequence):
        funcs = {'compliment':sequence.complement,
             'reverse compliment':sequence.reverse_complement,
             'transcribe':sequence.transcribe,
             'translate':sequence.translate}
    
        lst = [i.get() for i in self.temporary_list]
        for item in lst:
            if item:
                with open('test.txt','a') as f:
                    f.write(f'{str(funcs[item]())} \n')

    def validate_dna_sequence(self):
    
        sequence = Seq(self.entries.get())
        if sequence:
            valid_letters = set('AGCT')
            if set(sequence.upper()) - valid_letters:
 
                print(("Invalid DNA sequence. Only A, G, C, and T are allowed."))
            else:
                self.procedure(sequence)


class PageTwo(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='green').pack(fill='both',expand=True)



class PageThree(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.rowconfigure((0,1),weight=1,uniform='a')
        self.columnconfigure((0,1),weight=1,uniform='a')
        self.seq = Seq('AGTTTAATCGGCGTGGATTGCCGAACCCAGGTCCTATCAGTAC')
        self.make_graph()

    def make_graph(self):
        f_one = Figure(figsize=(5,5),dpi=100)
        a = f_one.add_subplot(111)
        a.bar([self.seq.count('A'),self.seq.count('T'),self.seq.count('G'),self.seq.count('C')],height=1)
        
        f_two = Figure(figsize=(5,5),dpi=100)
        b = f_two.add_subplot(111)
        b.pie([5,7,4,3])


        f_three = Figure(figsize=(5,5),dpi=100)
        c = f_three.add_subplot(111)
        c.hist([self.seq.count('A'),self.seq.count('T'),self.seq.count('G'),self.seq.count('C')],bins=2)


        f_four = Figure(figsize=(5,5),dpi=100)
        d = f_four.add_subplot(111)
        d.plot([1,2,3,4,5,6,7,8],[4,2,1,5,6,7,8,3])

        canvas_one = FigureCanvasTkAgg(f_one,self)     
        canvas_one.draw()

        canvas_two = FigureCanvasTkAgg(f_two,self)
        canvas_two.draw()

        canvas_three = FigureCanvasTkAgg(f_three,self)
        canvas_three.draw()

        canvas_four = FigureCanvasTkAgg(f_four,self)
        canvas_four.draw()


        canvas_one.get_tk_widget().grid(row=0,column=0,sticky=tk.NSEW)
        canvas_two.get_tk_widget().grid(row=0,column=1,sticky=tk.NSEW)
        canvas_three.get_tk_widget().grid(row=1,column=0,sticky=tk.NSEW)
        canvas_four.get_tk_widget().grid(row=1,column=1,sticky=tk.NSEW)



class PageFour(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='blue').pack(fill='both',expand=True)




class PageFive(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='orange').pack(fill='both',expand=True)




App("sequencer",(900,600))