

import tkinter as tk
from tkinter import ttk
from tkinter import Radiobutton, Button, Checkbutton

def select(event):
    selected_flavor = combo_box.get()
    label.config(text="Selected Flavor: " + selected_flavor)
    
def print_total():
    total = 0
    if size.get() == 1:
        total = total + 1
    elif size.get() == 2:
        total = total + 2
    elif size.get() == 3:
        total = total + 3
        
    if nTop.get() == 1:
        total += 1
    if cTop.get() == 1:
        total += 1 
    
        
        
    customer_name = entry_cust.get()    
    total_label.config(text="Total: $" + str(total) + "\nThank you, " + customer_name +"!")    
    
        
root=tk.Tk()
root.title("Order Ice Cream")

label_cust = tk.Label (root, text = 'Enter Customer Name: ')
label_cust.pack_configure()
entry_cust = tk.Entry(root)
entry_cust.pack_configure()

label = tk.Label(root, text = "Select Flavor: ")
label.pack(pady=10)

combo_box = ttk.Combobox(root, values=["Chocolate", "Strawberry", "Vanilla", "Tutti Fruitti"])
combo_box.set("Chocolate")
combo_box.pack(pady=10)

combo_box.bind("<<ComboboxSelected>>", select)

size=tk.IntVar()

size_label = tk.Label(root, text="Choose Size:")
size_label.pack(pady=10)
 
Radiobutton(root, text = 'Small', variable=size, value=1).pack(anchor=tk.CENTER)
Radiobutton(root, text = 'Medium', variable=size, value=2).pack(anchor=tk.CENTER)        
Radiobutton(root, text = 'Large', variable=size, value=3).pack(anchor=tk.CENTER)

check_label = tk.Label(root, text="Add toppings:")
check_label.pack(pady=10)

nTop = tk.IntVar()
Checkbutton(root, text="Add Nuts ($1)", variable = nTop).pack(padx=150, anchor=tk.W)
cTop = tk.IntVar()
Checkbutton(root, text="Add Whipped Cream ($1)", variable = cTop).pack(padx=150, anchor=tk.W)

#button to print total
button = Button(root, text = "Print Total", command=print_total)
button.pack(pady= 20)

# Create a label for showing the total at the bottom
total_label = tk.Label(root, text="Total: $0")
total_label.pack(pady=10)


root.mainloop()

    
    


