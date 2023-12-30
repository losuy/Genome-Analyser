# import tkinter as tk
# from Bio.Seq import Seq




# option = ['compliment','reverse compliment','transcribe','translate']

# app = tk.Tk()
# app.geometry("800x600")

# variable = tk.StringVar(app)



# # frame = tk.Frame(app,bg='red')
# # frame.pack(fill='both',expand=True) 
# # widget_frame = tk.Frame(frame,bg='yellow')
# # widget_frame.place(rely=0.1,relheight=0.2,relwidth=1)

# # check_frame = tk.Frame(frame,bg='blue')
# # check_frame.place(rely=0.3,relheight=0.4,relwidth=1)


# def procedure(sequence):
#     funcs = {'compliment':sequence.complement,
#              'reverse compliment':sequence.reverse_complement,
#              'transcribe':sequence.transcribe,
#              'translate':sequence.translate}
    
#     lst = [i.get() for i in c]
#     for item in lst:
#         if item:
#             with open('test.txt','a') as f:
#                 f.write(f'{str(funcs[item]())} \n')

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

# # entry = tk.Entry(widget_frame,textvariable='')
# # button = tk.Button(widget_frame,text='PRESS',command=validate_dna_sequence)
# # option_validate_button = tk.Button(check_frame,text='PRESS',command=validate_dna_sequence)
# # c = create_check_boxes(option)

# # option_validate_button.pack(side=tk.TOP,padx=10,anchor=tk.W,expand=True)
# # entry.pack(side='left',expand=True,fill='both')
# # button.pack(side='right',fill='both',expand=True)



# app.mainloop()


