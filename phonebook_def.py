
from collections import namedtuple
import os

contacts=[]
Contact=namedtuple("Contact",("name", "phone","birth_year"))


def load():
     if os.path.isfile("contacts.csv"):
        with open("contacts.csv","r") as dariush:
            for line in dariush:
                n,p,b=line[:-1].split(",")
                contact=Contact(n, p, b)
                contacts.append(contact)
        if len(contacts)>0:
            contacts.pop(0)
choice=input("""Welcome, please enter your choice:
1 \U0001f449 New
2 \U0001f449 list
3 \U0001f449 search
0 \U0001f449 exit \n""")
while choice != "0":
    if choice=="1":
        name=input("enter name: ")
        phone_number=input("enter phone number: ")
        birth_year=input("enter your birth name: ")
        contact=Contact(name, phone_number,birth_year)
        contacts.append(contact)
    elif choice =="2":
        print(contacts)
    elif choice =="3":
        name=input("enter name: ")
        for contact in contacts:
            if contact[0]==name:
                print(contact[1])
    elif choice =="3":
        name=input("enter name: ")
        for contact in contacts:
            if contact[0]==name:
                print(contact[1])
                break
        else:
            print("wrong name")
    choice=input("""enter your choice:
    1) \U0001f449 New,
    2) \U0001f449 list,
    3) \U0001f449 search,
    0) \U0001f449 exit\n """)  

def save():
    with open("contacts.csv","w") as dariush:
        dariush.write("name,phone,birth_year\n")
        for contact in contacts:
            dariush.write(f"{contact.name},{contact.phone},{contact.birth_year}\n")



              
