import tkinter as tk
from Bio.Seq import Seq




options = ['compliment','reverse compliment','transcribe','translate']

app = tk.Tk()
app.geometry("800x600")


frame = tk.Frame(app,bg='red')
frame.pack(fill='both',expand=True) 
widget_frame = tk.Frame(frame,bg='yellow')
widget_frame.place(x=9,y=10,relwidth=0.98,relheight=0.06)

check_frame = tk.Frame(frame,bg='blue')
check_frame.place(x=10,rely=0.09,relwidth=0.98,relheight=0.9)

sequence = Seq('AGTTAGTCCTAGTCCCTATA')

standard_option = tk.StringVar()
standard_option.set(options[1])
op = tk.StringVar()
op.set(standard_option.get())

# def select_caller(value):
#     op.set(standard_option.get())

def button_caller():
    pass

def procedure():
    funcs = {'compliment':sequence.complement,
             'reverse compliment':sequence.reverse_complement,
             'transcribe':sequence.transcribe,
             'translate':sequence.translate}
    
    text.insert(tk.END,funcs[standard_option.get()]() + '\n')
    
    

# def validate_dna_sequence():
#     sequence = Seq(entry.get())
#     if sequence:
#         valid_letters = set('AGCT')
#         if set(sequence.upper()) - valid_letters:
 
#             print(("Invalid DNA sequence. Only A, G, C, and T are allowed."))
#         else:
#             procedure(sequence)
        
    

# # def create_check_boxes(option):
# #     temporary_list = [tk.StringVar(value='') for i in option]
# #     # check_frame.rowconfigure([0,1,2,3,4],weight=1,uniform='a')
# #     check_frame.columnconfigure([0],weight=1,uniform='a')
# #     check_frame.rowconfigure([1],weight=1,uniform='a')

# #     for i in range(0,len(option)):
# #         frame = tk.Checkbutton(check_frame,text=option[i],variable=temporary_list[i],
# #                                onvalue=option[i],offvalue='')
# #         frame.pack(side=tk.TOP,anchor=tk.W,padx=10,expand=True)

# #     return temporary_list

drop_down = tk.OptionMenu(widget_frame,standard_option,*options)
text = tk.Text(check_frame)

button = tk.Button(widget_frame,text='PRESS',command=procedure)
# # option_validate_button = tk.Button(check_frame,text='PRESS',command=validate_dna_sequence)
# # c = create_check_boxes(option)

# # option_validate_button.pack(side=tk.TOP,padx=10,anchor=tk.W,expand=True)
widget_frame.columnconfigure((0,1,2),weight=1)
widget_frame.rowconfigure(0,weight=1)
drop_down.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW)
button.grid(row=0,column=2,sticky=tk.NSEW)
text.pack(expand=True,fill='both')

# lst = [i.get() for i in c]
#     for item in lst:
#         if item:
#             with open('test.txt','a') as f:
#                 f.write(f'{str(funcs[item]())} \n')
# Might come in handy

app.mainloop()


