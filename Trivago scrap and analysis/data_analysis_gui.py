import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import plotly.express as px
df=pd.read_csv("tourist places.csv")
df=df.sort_values(by="Title")
import Graph_code as gc
import time
from tkinter import *
import trivago_tk

def triv2():
    
    # Creating tkinter window
    window = tk.Tk()
    window.title('Graph Analysis')
    window.geometry('500x500')
    window.resizable(False, False)
    #window.eval('tk::PlaceWindow . center')
    radio = IntVar() 
    # label text for title
    ttk.Label(window, text = "Time v/s Average rate", 
              font = ("Times New Roman", 15)).place(relx = 0.5, rely = 0.1, anchor=CENTER)
      
    # label
    ttk.Label(window, text = "Select City :").place(x = 20, y = 80)
      
    # Combobox creation
    city_chs_plot = tk.StringVar()
    citychoosen = ttk.Combobox(window, width = 27, textvariable = city_chs_plot)
    def graph():
        city_name=citychoosen.get()
        print(city_name)
        star=radio.get()
        star1=str(star)
        maxp = float(e2.get())
        gc.plot_graph(city_name,star1,maxp)
        #print(n.get())

    def goHome():
        window.destroy()
        trivago_tk.homeWindow()
        
    # Adding combobox drop down list
    citychoosen['values'] = tuple(df.iloc[:,0])
    #citychoosen['values'] = ("jaipur","pushkar","ajmer")
      
    citychoosen.place(x = 220, y = 80)
    citychoosen.current()

    l3=tk.Label(window,text="Number of Stars")
    l3.place(x=20,y=120)
    r1=tk.Radiobutton(window,text="1 star",variable=radio,value=1)
    r1.place(x=220,y=120)
    r2=tk.Radiobutton(window,text="2 star",variable=radio,value=2)
    r2.place(x=220,y=140)
    r3=tk.Radiobutton(window,text="3 star",variable=radio,value=3)
    r3.place(x=220,y=160)
    r4=tk.Radiobutton(window,text="4 star",variable=radio,value=4)
    r4.place(x=220,y=180)
    r5=tk.Radiobutton(window,text="5 star",variable=radio,value=5)
    r5.place(x=220,y=200)

    def entryOpen():
        valChk = checkbox1.get()
        if valChk == 1:
            e2.config(state='normal')
            e2.delete(0, 'end')
        else:
            e2.delete(0, 'end')
            e2.insert(0, -1)
            e2.config(state='disabled')

    checkbox1 = IntVar()
    cb1=Checkbutton(window,text="Check this button if you want to enter maximum price",variable=checkbox1,onvalue=1,offvalue=0,command=entryOpen).place(x=20,y=230)
    
    l2=Label(window,text="Maximum Price").place(x=20,y=260)

    maxPrice = IntVar(window, value=-1)
    e2=Entry(window, state='disabled', textvariable=maxPrice)
    e2.place(x=220,y=260)

    b1=tk.Button(window,text="Plot Graph",bg="green",fg="white",command=graph)
    b1.place(x=20,y=300)
    btn2=Button(window,text="Home",bg="green",fg="white",command=goHome).place(x=100,y=300)

    window.mainloop()
