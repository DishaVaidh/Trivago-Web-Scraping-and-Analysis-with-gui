import pandas as pd
import numpy as np
import Data_extraction_gui
import data_analysis_gui
from tkinter import *
import requests as re

def homeWindow():
	a=Tk()
	a.title("Trivago Analysis Tool")
	a.geometry("500x500")
	a.resizable(False, False)
	#a.eval('tk::PlaceWindow . center')
	
	def func1():
	    a.destroy()
	    Data_extraction_gui.triv1()
	def func2():
	    a.destroy()
	    data_analysis_gui.triv2()

	def exitFunc():
		a.destroy()

	l=Label(a,text="Click this button to extract data")
	l.place(relx=0.5,rely=0.1,anchor=CENTER)
	b=Button(a,text="Data Extract",bg="green",fg="white",command=func1)
	b.place(relx=0.5,rely=0.2,anchor=CENTER)
	l2=Label(a,text="Click this button to visualise data")
	l2.place(relx=0.5,rely=0.3,anchor=CENTER)
	b1=Button(a,text="Data Analysis",bg="green",fg="white",command=func2)
	b1.place(relx=0.5,rely=0.4,anchor=CENTER)
	b2=Button(a,text="Exit",bg="green",fg="white",command=exitFunc).place(relx=0.5,rely=0.5,anchor=CENTER)
	a.mainloop()

if __name__ == '__main__':
	try:
		page = re.get("https://www.google.com").status_code
		homeWindow()
	except:
		print("No Internet Connection!")
	
