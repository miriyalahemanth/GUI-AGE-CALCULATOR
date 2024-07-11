from tkinter import *
from tkinter import messagebox
from datetime import date
root=Tk()
root.title("age calculator")
root.geometry("500x500")
def calculate():
    today=date.today()
    birthDate=date(int(e1.get()),int(e2.get()),int(e3.get()))
    if(today.year>birthDate.year):
        
        if(today.month>=birthDate.month and today.day>=birthDate.day):
            months=today.month-birthDate.month
            days=today.day-birthDate.day
            age=today.year-birthDate.year
            messagebox.showinfo("output",f"you are {age} years,{months} month,{days}day")
        
            
        elif(today.month<birthDate.month and today.day>=birthDate.day):
            total_months=12
            months=total_months-birthDate.month+today.month
            days=today.day-birthDate.day
            age=today.year-birthDate.year-1
            messagebox.showinfo("output",f"you are {age} years,{months} month,{days} day")
        elif(today.month<birthDate.month and today.day<birthDate.day):
            total_months=12
            months=(total_months-birthDate.month+today.month)-1
            days=(today.day-birthDate.day)-1
            age=today.year-birthDate.year-1
            messagebox.showinfo("output",f"you are {age} years,{months} month,{days} day")
        else:
            months=0
            days=0
    elif(today.year==birthDate.year):
        if(today.month>=birthDate.month and today.day>birthDate.day):
            age=today.year-birthDate.year
            months=today.month-birthDate.month
            days=today.day-birthDate.day
            messagebox.showinfo("output",f"you are {age} years,{months} month,{days} day")
        else:
            age=today.year-birthDate.year
            months=0
            days=0
            messagebox.showinfo("output",f"you are {age} years,{months} month,{days} day")
    else:
        messagebox.showinfo("output","error")
            
        
        
        
       
         
l1=Label(root,text="Birth Year",font="arial 15").place(x=50,y=50)
l2=Label(root,text="Birth Month",font="arial 15").place(x=50,y=150)
l3=Label(root,text="Birth Date",font="arial 15").place(x=50,y=250)
e1=Entry(font="arial 15",bd=5)
e1.place(x=250,y=50)
e2=Entry(font="arial 15",bd=5)
e2.place(x=250,y=150)
e3=Entry(font="arial 15",bd=5)
e3.place(x=250,y=250)
b=Button(root,text="Get Age",font="arial 15",command=calculate).place(x=150,y=350)
root.mainloop()
