import tkinter as tk

class App(tk.Tk):
    def __init__(self,title,size):
        super().__init__()

        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.resizable(0,0)
        self.main = Main(self)
        self.menu = Menu(self,self.main)

        self.mainloop()



class Menu(tk.Frame):
    def __init__(self,parent,main):
        super().__init__(parent)

        self.main = main
        self.create_widget()
        self.place(x=0,y=0,relwidth=0.3,relheight=1)

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
        self.frames = (PageOne,PageTwo,PageThree,PageFour,PageFive)
        self.pages = {}

        print(self.create_and_map_pages())
        self.place(relx=0.3,y=0,relwidth=0.7,relheight=1)
 

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
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='yellow').pack(fill='both',expand=True)



class PageTwo(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='red').pack(fill='both',expand=True)



class PageThree(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='green').pack(fill='both',expand=True)



class PageFour(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='blue').pack(fill='both',expand=True)



class PageFive(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,background='orange').pack(fill='both',expand=True)




App("sequencer",(800,600))