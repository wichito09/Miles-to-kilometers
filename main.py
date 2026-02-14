import tkinter as tk
from tkinter import ttk



def converting():
    '''Converts the entry_int value into kilometers'''
    try:
        miles = entry_int.get()
        kilometer_value = round(miles * 1.60934, 2)
        output_string.set(f'{kilometer_value}\n Kilometers')
    except tk.TclError:
        output_string.set('ERROR: please \n enter a number')

# window
window = tk.Tk()
window.title('converter')
window.geometry('600x400')
icon = tk.PhotoImage(file='asests/mtok.png')
window.iconphoto(True,icon)

# title
main_title = tk.Label(master=window, text='Miles \n to Kilometer',font='arial 38 bold')
main_title.pack()

# input text & button
input_frame = tk.Frame(master=window,pady=10)
entry_int = tk.IntVar()
entry = tk.Entry(master=input_frame,textvariable=entry_int,font=38)
button = tk.Button(master=input_frame,text='convert',command=converting,bg='#ff5454',fg="#ffffff")
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack()

# output label
output_string = tk.StringVar()
output_label = tk.Label(master=window,text='TEMP',font='impact 38',textvariable=output_string)
output_label.pack()

# main loop
window.mainloop()
