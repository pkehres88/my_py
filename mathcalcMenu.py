# -*- coding: utf-8 -*-

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
        
        #Display the result in a messagebox
        messagebox.showinfo("Pesticide application in gallons per minute is: {gallonsPerMinute}")
    except ValueError:
        messagebox.showerror("Invalid values.", "Please enter valid numbers.")        

        
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

# Create and place calculation button
calculate_button = tk.Button(root, text="Calculate pesticide application rate", command=calculate_GPM())
calculate_button.grid(row=3, column=0, columnspan=2, pady=10) 

