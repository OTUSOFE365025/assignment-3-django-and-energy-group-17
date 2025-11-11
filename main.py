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

#REMOVE THESE AFTER FIRST RUN OF THE CODE

Products.objects.create(upc="78234", name="Apple", price=3.47)
Products.objects.create(upc="14567", name="Banana", price=2.89)
Products.objects.create(upc="90521", name="Orange", price=4.32)
Products.objects.create(upc="63412", name="Grapes", price=1.76)
Products.objects.create(upc="21987", name="Mango", price=2.15)
Products.objects.create(upc="47823", name="Pear", price=5.68)
Products.objects.create(upc="89135", name="Peach", price=3.92)
Products.objects.create(upc="35678", name="Cherry", price=4.54)
Products.objects.create(upc="72019", name="Strawberry", price=6.21)
Products.objects.create(upc="46102", name="Blueberry", price=2.74)
Products.objects.create(upc="89346", name="Raspberry", price=1.88)
Products.objects.create(upc="50721", name="Watermelon", price=3.67)
Products.objects.create(upc="31258", name="Cantaloupe", price=7.43)
Products.objects.create(upc="67920", name="Pineapple", price=2.06)
Products.objects.create(upc="24813", name="Kiwi", price=5.81)
Products.objects.create(upc="13579", name="Plum", price=1.99)
Products.objects.create(upc="56490", name="Apricot", price=4.27)
Products.objects.create(upc="90876", name="Blackberry", price=3.55)
Products.objects.create(upc="43218", name="Grapefruit", price=2.42)
Products.objects.create(upc="61745", name="Nectarine", price=6.78)

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
