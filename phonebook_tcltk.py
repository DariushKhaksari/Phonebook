from tkinter import *
window=Tk()
frame_right=Frame()
frame_right.pack(side=LEFT)
frame_left=Frame()
frame_left.pack(side=RIGHT)
#NAME
frame_name=Frame(frame_right)
frame_name.pack()
lable_name=Label(frame_name,text="name: ")
lable_name.pack(side=LEFT)
input_name=Entry(frame_name)
input_name.pack(side=RIGHT)
#MOBILE
frame_mobile=Frame(frame_right)
frame_mobile.pack()
lable_mobile=Label(frame_mobile,text="mobile: ")
lable_mobile.pack(side=LEFT)
input_mobile=Entry(frame_mobile)
input_mobile.pack(side=RIGHT)
#AGE
frame_age=Frame(frame_right)
frame_age.pack()
lable_age=Label(frame_age,text="age: ")
lable_age.pack(side=LEFT)
input_age=Entry(frame_age)
input_age.pack(side=RIGHT)
#SAVE
frame_save=Frame(frame_left)
frame_save.pack()
button_save=Button(frame_save,text="Save")
button_save.pack()
#CLEAR
button_clear=Button(frame_save,text="Clear")
button_clear.pack()
window.mainloop()


