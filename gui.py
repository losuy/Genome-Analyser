import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import threading
from Bio.Seq import Seq
from Bio import SeqIO
import math
from collections import Counter
from PIL import Image
from PIL import ImageTk
import customtkinter as CTk
from tkinter import ttk
from pathlib import Path

class App(CTk.CTk):
    def __init__(self,title,size):
        super().__init__()

        self.geometry(f"{size[0]}x{size[1]}")

        self.title(title)
        # self.resizable(0,0)
        self.icon = ImageTk.PhotoImage(Image.open('project/images/dna.png'))
        self.iconbitmap()
        self.iconphoto(False, self.icon)
        self.app_frame = App_frame(self)
        self.main = Main(self.app_frame)
        self.menu = Menu(self.app_frame,self.main)

        self.mainloop()


class App_frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.image = ImageTk.PhotoImage(Image.open('project/images/black.png'))
        self.label = tk.Label(self,image=self.image)
        self.label.place(x=0,y=0)

        self.place(x=0,y=0,relwidth=1,relheight=1)


class Menu(CTk.CTkFrame):
    def __init__(self,parent,main,):
        super().__init__(parent,corner_radius=20)


        self.image_1 = ImageTk.PhotoImage(Image.open('project/images/directory.png'))
        self.image_2 = ImageTk.PhotoImage(Image.open('project/images/operation.png'))
        self.image_3 = ImageTk.PhotoImage(Image.open('project/images/output.png'))
        self.image_4 = ImageTk.PhotoImage(Image.open('project/images/graph.png'))
        self.main = main
        self.configure(fg_color='black',bg_color="black")

        self.create_widget()
        self.place(x=10,y=10,relwidth=0.31,relheight=0.97)

    def create_widget(self):
       button_1 = CTk.CTkButton(self,text = 'Directory',border_width=5,border_color='black',
       image=self.image_1,fg_color='#559202',corner_radius=15,hover=True,hover_color='#7A1042',border_spacing=3,
       command = lambda: self.main.show_frame(page_name ='PageOne'))
       button_2 = CTk.CTkButton(self,text = 'Operation',border_width=5,border_color='black',
       image=self.image_2,fg_color='#FF0000',corner_radius=15,hover=True,hover_color='#00A933',border_spacing=3,
       command = lambda: self.main.show_frame(page_name ='PageTwo'))
       button_3 = CTk.CTkButton(self,text = 'Output',border_width=5,border_color='black',
       image=self.image_3,fg_color='#0005FF',corner_radius=15,hover=True,hover_color='#FF8000',border_spacing=3,
       command = lambda:self. main.show_frame(page_name ='PageThree'))
       button_4 = CTk.CTkButton(self,text = 'Graph',border_width=5,border_color='black',
       image=self.image_4,fg_color='#730665',corner_radius=15,hover=True,hover_color='#6C770F',
       border_spacing=3,command = lambda: self.main.show_frame(page_name ='PageFour'))
       
       
       self.rowconfigure((1,2,3,4),weight=1)
       self.columnconfigure(0,weight=1,uniform='a')
       
       button_1.grid(row=1,column=0,sticky='nsew')
       button_2.grid(row=2,column=0,sticky='nsew')
       button_3.grid(row=3,column=0,sticky='nsew')
       button_4.grid(row=4,column=0,sticky='nsew')

class Main(CTk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,corner_radius=30)
    
        self.frames = (PageFour,PageThree,PageTwo,PageOne)
        self.pages = {}

        self.create_and_map_pages()
        self.pages['PageOne'].pagetwo = self.pages['PageTwo']
        self.pages['PageTwo'].pagethree = self.pages['PageThree']
        self.pages['PageTwo'].pagefour = self.pages['PageFour']
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
        self.after(100,frame.tkraise())
        # frame.tkraise()



class PageOne(CTk.CTkFrame):
    def __init__(self,parent):
        self.pagetwo = None
        super().__init__(parent)

        self.frame = CTk.CTkFrame(self,fg_color='#559202',corner_radius=15,bg_color='black')
        self.image_1 = CTk.CTkImage(Image.open('project/images/download_directory.png'))
        self.image_2 = CTk.CTkImage(Image.open('project/images/send.png'))
        self.Directory_frame = CTk.CTkFrame(self.frame,corner_radius=0,fg_color='#A6A6A6')
        self.Directory_frame.rowconfigure((0,1),weight=1)
        self.Directory_frame.columnconfigure((0,1,2,3),weight=1)
        self.filepath = tk.StringVar()
        self.Frame_pack()
        self.Directory()


    def Frame_pack(self):
        self.frame.pack(fill='both',expand=True)
        self.Directory_frame.place(rely=0.1,relheight=0.7,relwidth=1)
    

    def get_File(self):
        '''Using a tkinter function filedialog.askopenfilename to ask for
            directory where we want to put downloaded file'''
        folder_name = tk.filedialog.askopenfilename(
                    initialdir=Path.home() / 'Downloads',title="Dialog box")
        self.filepath.set(folder_name)

    def Directory(self):
        label=CTk.CTkLabel(self.Directory_frame,text="Directory:",font=('Calibri', 18))
        entry=CTk.CTkEntry(self.Directory_frame,textvariable=self.filepath)
        label.grid(row=0,column=0,sticky='ew')
        entry.grid(row=0,column=1,sticky='ew',columnspan=2)
        CTk.CTkButton(self.Directory_frame,width=4,height=45,image=self.image_1,corner_radius=10,border_width=5,border_color='#A6A6A6',text="",fg_color='#559202',command=self.get_File).grid(row=0,column=3,sticky ='ew' )
        CTk.CTkButton(self.Directory_frame,width=100,height=35,fg_color='#559202',image=self.image_2,text="send",command=self.check_valid_file).grid(row=1,column=1,sticky='ne')

    def check_valid_file(self):
        if self.filepath.get().split('/')[-1].split('.')[-1] == 'fna':
            self.pagetwo.retrieve_data(self.filepath.get())
        print('error')



class PageTwo(CTk.CTkFrame):
    OPTIONS = ['complement','reverse complement','transcribe','translate'] 

    def __init__(self,parent):
        self.pagethree = None
        self.pagefour = None
        super().__init__(parent)

        self.main_frame = CTk.CTkFrame(self,fg_color='#FF0000',corner_radius=15,bg_color='black')
        self.widget_frame = CTk.CTkFrame(self.main_frame,bg_color='white')
        self.text_frame = CTk.CTkFrame(self.main_frame,)

        self.standard_option = tk.StringVar()
        self.standard_option.set(self.OPTIONS[1])
        self.sequence = None
        self.Buttons()
        self.DropDown()
        self.pack_frames()
        self.scrollbar = self.Scrollbar()
        self.text = self.Text_loader()
        self.scrollbar.configure(command=self.text.yview)


    def retrieve_data(self,file):
        for seq_record in SeqIO.parse(file, "fasta"):
            if len(seq_record.seq) % 3 != 0:
                closest_multiple_of_three = math.ceil(len(seq_record.seq)/3) * 3
                value_to_add = closest_multiple_of_three -len(seq_record.seq)
                seq_record.seq += (value_to_add*'N')
        self.sequence = seq_record
        self.send_value(seq_record.seq,seq_record.seq.translate())
        self.text.delete('1.0',tk.END)
        self.text.insert(tk.END,self.sequence.seq + '\n')

    def pack_frames(self):
        self.main_frame.pack(fill='both',expand=True)
        self.widget_frame.place(x=9,y=10,relwidth=0.98,relheight=0.06)
        self.text_frame.place(x=10,rely=0.09,relwidth=0.98,relheight=0.9)

    def Buttons(self):
        button = CTk.CTkButton(self.widget_frame,text='PRESS',command=self.procedure)
        button.grid(row=0,column=2,sticky='nsew')   

    def DropDown(self):
        self.widget_frame.columnconfigure((0,1,2),weight=1)
        self.widget_frame.rowconfigure(0,weight=1)
        drop_down = ttk.Combobox(self.widget_frame,textvariable=self.standard_option,values=self.OPTIONS,state='readonly',width=80)
        drop_down.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW)

    def Text_loader(self):
        text = CTk.CTkTextbox(self.text_frame,font=('Calibri', 18),
                              yscrollcommand=self.scrollbar.set,activate_scrollbars=False)
        text.pack(expand=True,fill='both')
        return text
    
    
    def Scrollbar(self):
        scrollbar = CTk.CTkScrollbar(self.text_frame)
        scrollbar.pack(side='right',fill='y')
        return scrollbar
    
    def procedure(self):
        
        try:
            funcs = {'complement':self.sequence.seq.complement,
                'reverse complement':self.sequence.seq.reverse_complement,
                'transcribe':self.sequence.seq.transcribe}
            if self.standard_option.get() == 'translate':
                option = 'translate'
                sequence = self.sequence.seq.translate().split('*')
                self.pagethree.retrieve_data(sequence,option)
            else:
                option = funcs[self.standard_option.get()]
                sequence = funcs[self.standard_option.get()]()
                self.pagethree.retrieve_data(sequence,option)
        except AttributeError:
            self.text.insert(tk.END,'Nothing to processed yet')


    def send_value(self,sequence,translated_sequence):
        self.pagefour.retrieve_data(sequence,translated_sequence)
        

    # def validate_dna_sequence(self):
    
    #     sequence = Seq(self.entries.get())
    #     if sequence:
    #         valid_letters = set('AGCT')
    #         if set(sequence.upper()) - valid_letters:
 
    #             print(("Invalid DNA sequence. Only A, G, C, and T are allowed."))
    #         else:
    #             self.procedure(sequence)



class PageThree(CTk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.display_1 =  None
        self.display_2 = None
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.display_1,self.text_1 = self.Display_1()
        self.display_2,self.text_2 = self.Display_2()

    def Display_1(self):
        frame = CTk.CTkFrame(self,corner_radius=30,bg_color='black')
        frame.grid(row=0,column=0,sticky='nsew')
        scrollbar = CTk.CTkScrollbar(frame)
        scrollbar.pack(side='right',fill='y')
        text = CTk.CTkTextbox(frame,font=('Calibri', 18),yscrollcommand=scrollbar.set,activate_scrollbars=False)
        # text.config(state='disabled')
        scrollbar.configure(command=text.yview)
        text.pack(fill='both',expand=True)
    
        return frame,text

    def Display_2(self):
        frame = CTk.CTkFrame(self,corner_radius=30,bg_color='black')
        frame.grid(row=0,column=0,sticky='nsew')
        scrollbar = CTk.CTkScrollbar(frame)
        scrollbar.pack(side='right',fill='y')
        text = CTk.CTkTextbox(frame,font=('Calibri', 18),yscrollcommand=scrollbar.set,activate_scrollbars=False)
        # text.config(state='disabled'cd )
        scrollbar.configure(command=text.yview)
        text.pack(fill='both',expand=True)
          
        return frame,text
    
    def retrieve_data(self,sequence,option):
        if option == 'translate':
            self.text_2.delete("1.0", tk.END)
            for line in sequence:
                self.text_2.insert(tk.END,str(line)+'\n')
            self.display_2.tkraise()
        else:
            self.text_1.delete('1.0',tk.END)
            self.after(10,self.text_1.insert(tk.END,sequence))
            self.display_1.tkraise()

class PageFour(CTk.CTkFrame):
    GRAPH = ['pie','bases','amino acid','all']
    def __init__(self,parent):
        super().__init__(parent)
        
        self.main_frame = CTk.CTkFrame(self)
        self.option_frame = CTk.CTkFrame(self.main_frame)
        self.graph_frame = CTk.CTkFrame(self.main_frame)
        self.error_frame = CTk.CTkFrame(self.graph_frame)
        self.error_label = CTk.CTkLabel(self.error_frame,text='Nothing to see yet',font=('Open sans',34),anchor='n')
        self.error_label.pack(expand=True,fill='both')
        self.graph_frame.rowconfigure(0,weight=1)
        self.graph_frame.columnconfigure(0,weight=1)
        self.error_frame.grid(row=0,column=0,sticky='nsew')
        self.standard_graph = tk.StringVar()
        self.standard_graph.set(self.GRAPH[len(self.GRAPH)-1])
        self.seq = None
        self.translated_seq = None
        self.package_frame()
        self.DropDown()
        self.graph_map = None
        

    def package_frame(self):
        self.main_frame.pack(fill='both',expand=True)
        self.option_frame.place(x=9,y=10,relwidth=0.98,relheight=0.06)
        self.graph_frame.place(x=10,rely=0.09,relwidth=0.98,relheight=0.9)

    def DropDown(self):
        self.option_frame.columnconfigure((0,1),weight=1)
        self.option_frame.rowconfigure((0,1),weight=1)
        drop_down = ttk.Combobox(self.option_frame,textvariable=self.standard_graph,values=self.GRAPH,state='readonly')
        drop_down.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW)
        drop_down.bind('<<ComboboxSelected>>',self.dropdown_command)
    def make_bases_graph(self):
        
        frame = CTk.CTkFrame(self.graph_frame)
        frame.grid(row=0,column=0,sticky='nsew')
        f_one = Figure(figsize=(5,5),dpi=100)
        a = f_one.add_subplot(111)
        a.bar(list(self.seq.keys()),height=list(self.seq.values()))
        
        canvas_one = FigureCanvasTkAgg(f_one,frame)     
        canvas_one.draw()

        canvas_one.get_tk_widget().pack(expand=True,fill='both')
        return frame

    def make_pie_graph(self):
        
        frame = CTk.CTkFrame(self.graph_frame)
        frame.grid(row=0,column=0,sticky='nsew')
        f_two = Figure(figsize=(5,5),dpi=100)
        b = f_two.add_subplot(111)
        b.pie(self.seq.values(), labels=self.seq.keys(), autopct='%1.1f%%', startangle=90)
      
        canvas_two = FigureCanvasTkAgg(f_two,frame)
        canvas_two.draw()

        canvas_two.get_tk_widget().pack(expand=True,fill='both')
        return frame


    def make_Amino_graph(self):
        
        frame = CTk.CTkFrame(self.graph_frame,corner_radius=15,bg_color='black')
        frame.grid(row=0,column=0,sticky='nsew')
        f_three = Figure(figsize=(5,5),dpi=100)
        c = f_three.add_subplot(111)
        c.bar(list(self.translated_seq.keys()),height=list(self.translated_seq.values()))

        canvas_three = FigureCanvasTkAgg(f_three,frame)
        canvas_three.draw()

        canvas_three.get_tk_widget().pack(expand=True,fill='both')
        return frame
    
    def make_all_graph(self):

        frame = tk.Frame(self.graph_frame)
        
        f_two = Figure(figsize=(5,5),dpi=100)
        a = f_two.add_subplot(111)
        a.bar(list(self.seq.keys()),height=list(self.seq.values()))
        
        f_one = Figure(figsize=(5,5),dpi=100)
        b = f_one.add_subplot(111)
        b.pie(self.seq.values(), labels=self.seq.keys(), autopct='%1.1f%%', startangle=90)


        f_three = Figure(figsize=(5,5),dpi=100)
        c = f_three.add_subplot(111)
        c.bar(list(self.translated_seq.keys()),height=list(self.translated_seq.values()))

        canvas_one = FigureCanvasTkAgg(f_one,frame)     
        canvas_one.draw()

        canvas_two = FigureCanvasTkAgg(f_two,frame)
        canvas_two.draw()

        canvas_three = FigureCanvasTkAgg(f_three,frame)
        canvas_three.draw()

        # canvas_one.get_tk_widget().grid(row=0,column=1,sticky=tk.NSEW)
        canvas_one.get_tk_widget().place(relx=0+0.55,rely=0,relheight=0.5,relwidth=0.55)
        # canvas_two.get_tk_widget().grid(row=0,column=0,sticky=tk.NSEW)
        canvas_two.get_tk_widget().place(relx=0,rely=0,relheight=0.5,relwidth=0.55)
        canvas_three.get_tk_widget().place(relx=0,rely=0+0.5,relheight=0.5,relwidth=1)
        frame.grid(row=0,column=0,sticky='nsew')
        return frame
    
    def dropdown_command(self,event):
        try:
            self.graph_map[self.standard_graph.get()].tkraise()
        except TypeError:
            self.error_frame.tkraise()



    def retrieve_data(self,sequence,translated):
        self.seq = Counter(sequence)
        del self.seq['N']
        self.translated_seq = Counter(translated)
        print(self.seq,'\n',self.translated_seq)
        self.graph_map = {'pie':self.make_pie_graph(),'bases':self.make_bases_graph(),
                       'amino acid':self.make_Amino_graph(),'all':self.make_all_graph()}
        




App("sequencer",(1100,600))

# i am not writing comments