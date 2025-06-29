# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import messagebox

# Function to calculate pesticide application rate in gallons per minute 
def calculate_GPM():
    try:
        # Get values entered by user
        gallonsPerAcre = float(entry_gallonsPerAcre.get())
        milesPerHour = float(entry_milesPerHour.get())
        nozzleSpacing = float(entry_nozzleSpacing.get())
                #Calculate gallons per minute
        gallonsPerMinute = (gallonsPerAcre * milesPerHour * nozzleSpacing) / 5940
        label_GPM.config(text=f"Application Rate: {gallonsPerMinute:.2f} GPM")
    except ValueError:
        messagebox.showerror("Invalid entry", "Please enter valid numbers")

        
# Initialize tkinter main window
root = tk.Tk()
root.title("Pesticide Application")

# Create Labels and entry fields
label_gallonsPerAcre = tk.Label(root, text="Enter gallons per acre:")
label_gallonsPerAcre.grid(row=0, column=0, padx=10, pady=10)

entry_gallonsPerAcre = tk.Entry(root)
entry_gallonsPerAcre.grid(row=0, column=1, padx=10, pady=10)

label_milesPerHour = tk.Label(root, text="Enter miles per hour:")
label_milesPerHour.grid(row=1, column=0, padx=10, pady=10)

entry_milesPerHour = tk.Entry(root)
entry_milesPerHour.grid(row=1, column=1, padx=10, pady=10)

label_nozzleSpacing = tk.Label(root, text="Enter nozzle spacing in inches:")
label_nozzleSpacing.grid(row=2, column=0, padx=10, pady=10)

entry_nozzleSpacing = tk.Entry(root)
entry_nozzleSpacing.grid(row=2, column=1, padx=10, pady=10) 

label_GPM = tk.Label(root, text = "Application Rate:")
label_GPM.grid(row=4, column=0, padx=10, pady=10)

# Create and place calculation button
calculate_button = tk.Button(root, text="Calculate pesticide application rate", command=calculate_GPM)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10) 

# Start the main loop
root.mainloop()

