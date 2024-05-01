import  tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

style = ttk.Style(root)
root.tk.call('source', 'forest-dark.tcl')
style.theme_use('forest-dark')

frame = ttk.Frame(root)
frame.pack()

widget_frame = ttk.LabelFrame(frame, text = "Inset Row")
widget_frame.grid(row=0, column=0)
name_entry = ttk.Entry(widget_frame)
name_entry.grid(row=0, column=1, sticky="ew")



root.mainloop()
