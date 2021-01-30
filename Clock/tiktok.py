from tkinter import ttk
from tkinter import Tk
from time import strftime

root = Tk()
root.title('FlavorFlav')

def time():
    string = strftime('%H:%M:%S %p')
    ttk.Label.config(text=string)
    ttk.Label.after(1000, time)


ttk.Label = ttk.Label(root, font=('ds-digital',  100), background = 'black', foreground = 'cyan')
ttk.Label.pack(anchor='center')

time()

root.mainloop()
