import pandas as pd
import numpy as np
from tkinter import ttk
import extraction_code as ec
import trivago_tk
from tkcalendar import Calendar
import datetime
df=pd.read_csv("tourist places.csv")
df=df.sort_values(by="Title")
from tkinter import *
def triv1():
    b=Tk()
    b.title("Scrap Data of Trivago")
    b.geometry("500x500")
    b.resizable(False, False)
    #b.eval('tk::PlaceWindow . center')
    lbl=Label(b)
   
    # label
    l1=Label(b, text = "Select City ").place(x=20,y=20)

    def func():
        city=citychoosen1.get()
        #sd_str=e2.get()
        sd_str = str(e2.get_date())
        sd_str = datetime.datetime.strptime(sd_str,"%m/%d/%y").strftime("%Y-%m-%d")
        
        st=var.get()
        ac=checkbox1.get()
        print(city,sd_str,st,ac)
        ec.function(city,sd_str,st,ac)

    def goHome():
        b.destroy()
        trivago_tk.homeWindow()

    citychoosen1 = ttk.Combobox(b, width = 27)

    # Adding combobox drop down list
    citychoosen1['values'] = tuple(df.iloc[:,0])
    #citychoosen1['values'] = ("jaipur","pushkar","ajmer")
      
    citychoosen1.place(x=220,y=20)
    citychoosen1.current()

    l2=Label(b,text="Checkin Date").place(x=20,y=60)
    #e2=Entry(b)
    #e2.place(x=220,y=60)
    e2 = Calendar(b, selectmode = 'day',year = datetime.datetime.now().year)
    e2.place(x=220,y=60)

    var = IntVar()
    checkbox1 = IntVar()
    l3=Label(b,text="Number of Stars").place(x=20,y=240)
    r1=Radiobutton(b,text="1 star",variable=var,value=1)
    r1.place(x=220,y=240)
    r2=Radiobutton(b,text="2 star",variable=var,value=2)
    r2.place(x=220,y=260)
    r3=Radiobutton(b,text="3 star",variable=var,value=3)
    r3.place(x=220,y=280)
    r4=Radiobutton(b,text="4 star",variable=var,value=4)
    r4.place(x=220,y=300)
    r5=Radiobutton(b,text="5 star",variable=var,value=5)
    r5.place(x=220,y=320)
    #rad()
    #l4=Label(b,text="Check this button if you want AC").place(x=20,y=210)
    cb1=Checkbutton(b,text="Check this button if you want AC",variable=checkbox1,onvalue=1).place(x=20,y=360)


    btn=Button(b,text="Scrap Data",bg="green",fg="white",command=func).place(x=20,y=420)
    lbl.place(x=20,y=240)#empty label and it is filled when the function is call
    btn2=Button(b,text="Home",bg="green",fg="white",command=goHome).place(x=100,y=420)

    b.mainloop()
