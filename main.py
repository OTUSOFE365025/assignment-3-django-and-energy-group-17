############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

# Import tkinter and related modules for gui
import tkinter as tk
from tkinter import ttk, messagebox

# import random module to emulate scanning
import random

# global subtotal variable
subtotal = 0.0

# Event handling
def on_button_click():
    global subtotal
    upcList = list(Products.objects.all())
    if not upcList:
        messagebox.showwarning("No Products", "No products found in the UPC list.")
        return
    
    product = random.choice(upcList)
    tree.insert("", "end", values=(product.upc, product.name, product.price))

    subtotal += float(product.price)
    label.config(text=f"Subtotal = ${subtotal:.2f}")

############################################################################
## START OF APPLICATION
############################################################################

root = tk.Tk()

root.title("Cash Register Scanner")

root.geometry("400x300")

topFrame = tk.Frame(root, borderwidth=2, relief="solid")
topFrame.pack(side="top", fill="x")

tableFrame = tk.Frame(root)
tableFrame.pack(side="top", fill="both", expand=True)

label = tk.Label(topFrame, text="Subtotal = $0.00")
label.pack(side="left", padx=10, pady=10)

button = tk.Button(topFrame, text="Scan Item", command=on_button_click)
button.pack(side="right", padx=10, pady=10)

columns = ("UPC", "Name", "Price")

tree = ttk.Treeview(tableFrame, columns=columns, show="headings")

tree.heading("UPC", text="UPC")
tree.heading("Name", text="Name")
tree.heading("Price", text="Price")

tree.column("UPC", width=75, anchor="center")
tree.column("Name", width=150, anchor="center")
tree.column("Price", width=75, anchor="center")

scrollbar = ttk.Scrollbar(tableFrame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand="true")
scrollbar.pack(side="right", fill="y")

root.mainloop()
