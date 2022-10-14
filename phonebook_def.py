from tkinter import*
from tkinter.ttk import *
from collections import namedtuple
import os

contacts=[]
contacts=namedtuple("Contact",("name", "phone","birth_year"))
main_window=Tk

def load():
     if os.path.isfile("contacts.csv"):
        with open("contacts.csv","r") as f:
            for line in f:
                n,p,b=line[:-1].split(",")
                contact=Contact(n, p, b)
                contacts.append(contact)
        if len(contacts)>0:
            contacts.pop(0)

def save():
    with open("contacts.csv", "w") as f :
        f.write("Name,Phone, Birth_year\n")
        for contact in contacts:
            f.write(f"{contact.Name},{contact.Phone},{contact.Birth_year}\n")



def refresh_list():
    tv.delete(*tv.get_children())
    for i, contact in enumerate(contacts):
        tv.insert(parent="", indext=i, iid=i, text="", values=contact)

def show_add_from():
    add_from=Tk()

    name_Var=StringVar(add_form)
    phone_Var=StringVar(ad_form)
    birth_Var=IntVar(add_from)
    def add_contact():
        contact=Contact(name_Var.get(), phone_Var.get(), birth_Var.get())
        contacts.append(contact)               
