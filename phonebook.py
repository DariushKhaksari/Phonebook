contacts=[]
choice=input("""Welcome, please enter your choice:
1 \U0001f449 New,
2 \U0001f449 list,
3 \U0001f449 search,
0 \U0001f449 exit: """)
while choice != "0":
    if choice=="1":
        name=input("enter name: ")
        phone_number=input("enter phone number: ")
        contact=[name,phone_number]
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
            if contact[0]!=name:
                print("no")
    choice=input("""enter your choice:
    1) \U0001f449 New,
    2) \U0001f449 list,
    3) \U0001f449 search,
    0) \U0001f449 exit: """)                           
           
    