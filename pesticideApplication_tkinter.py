# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import messagebox

# Function to calculate total manufacturing cost 
def calculate_TMC():
    try:
        # Get values entered by user
        costMaterials = float(entry_costMaterials.get())
        costLabor = float(entry_costLabor.get())
        costOverhead = float(entry_costOverhead.get())
        #Calculate total manufacturing cost
        TMC = costMaterials + costLabor + costOverhead
        label_TMC.config(text=f"Total Manufacturing Cost: {TMC:.2f} ")
    except ValueError:
        messagebox.showerror("Invalid entry", "Please enter valid numbers")

        
# Initialize tkinter main window
root = tk.Tk()
root.title("Total Manufacturing Cost")

# Create Labels and entry fields
label_costMaterials = tk.Label(root, text="Enter direct cost of materials:")
label_costMaterials.grid(row=0, column=0, padx=10, pady=10)

entry_costMaterials = tk.Entry(root)
entry_costMaterials.grid(row=0, column=1, padx=10, pady=10)

label_costLabor = tk.Label(root, text="Enter direct cost of labor:")
label_costLabor.grid(row=1, column=0, padx=10, pady=10)

entry_costLabor = tk.Entry(root)
entry_costLabor.grid(row=1, column=1, padx=10, pady=10)

label_costOverhead = tk.Label(root, text="Enter manufacturing overhead:")
label_costOverhead.grid(row=2, column=0, padx=10, pady=10)

entry_costOverhead = tk.Entry(root)
entry_costOverhead.grid(row=2, column=1, padx=10, pady=10) 

label_TMC = tk.Label(root, text = "Total Manufacturing Cost:")
label_TMC.grid(row=4, column=0, padx=10, pady=10)

# Create and place calculation button
calculate_button = tk.Button(root, text="Calculate total manufacturing cost", command=calculate_TMC)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10) 

# Start the main loop
root.mainloop()

