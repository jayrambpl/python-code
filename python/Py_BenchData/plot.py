import os
import json
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
# import benchdata as bd

from tkinter import messagebox as mb

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#00FF00", "#FF0000", "#0000FF", "#FFFF00", "#FF00FF"])

def read_history(key):
    history_path = os.path.join(os.getcwd(), "history.json")
    if not os.path.exists(history_path):
        mb.showerror("Error", "History database not found.")
        return None
    
    try:
        with open('history.json', 'r') as file:
            historical_data = json.load(file)
    except FileNotFoundError:
        historical_data = {}

    if key in historical_data:
        return historical_data[key]
    else:
        return None
        
# ------------------------

key = "2024-09-01 12:34:56"

db= read_history(key=key)

bench_plt_data = { 
                "CONFIRMED": "",
                "PROPOSED": "",
                "AVAILABLE": "",
}
upcoming_plt_data = {
                "WITHIN15": "",
                "WITHIN30": "",
                "WITHIN60": "",
                "WITHIN90": "",
                "AFTER90": ""
}
bench_plt_data["CONFIRMED"] = db["CONFIRMED"]
bench_plt_data["PROPOSED"] = db["PROPOSED"]
bench_plt_data["AVAILABLE"] = db["AVAILABLE"]

upcoming_plt_data["WITHIN15"] = db["WITHIN15"]  
upcoming_plt_data["WITHIN30"] = db["WITHIN30"]
upcoming_plt_data["WITHIN60"] = db["WITHIN60"]
upcoming_plt_data["WITHIN90"] = db["WITHIN90"]
upcoming_plt_data["AFTER90"] = db["AFTER90"]

pig1, ax1 = plt.subplots()
ax1.set_title("Bench Data")
ax1.pie(list(bench_plt_data.values()), labels=list(bench_plt_data.keys()), autopct='%1.1f%%',   )
# plt.show()

pig2, ax2 = plt.subplots()
ax2.set_title("Upcoming Bench Data")
ax2.pie(list(upcoming_plt_data.values()), labels=list(upcoming_plt_data.keys()), autopct='%1.1f%%',   )
# plt.show()

root = tk.Tk()
root.state("zoomed")

frame1 = tk.Frame(root)
frame1.pack(fill=tk.BOTH, expand=True )
canvas1 = FigureCanvasTkAgg(pig1, frame1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=True )

canvas2 = FigureCanvasTkAgg(pig2, frame2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()

