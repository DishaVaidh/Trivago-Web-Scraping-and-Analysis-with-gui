import pandas as pd
import numpy as np
import plotly.express as px
import webbrowser
import plotly
from flask import Flask, request, render_template

def plot_graph(c,maxPrice,st=0):
    app = Flask(__name__, template_folder='.')
    print(c)
    print(type(st))
    df1=pd.read_csv("C:\\trivago_data\\"+c+st+"star"+".csv")
    #df1 = pd.read_csv("jaipur.csv")
    
    if(maxPrice != -1):
        df1=df1.drop(df1[df1['Rate'] > maxPrice].index)
    #print(df1.describe())
    g=df1.groupby(by='checkin')
    a=g['Rate'].agg(np.mean)
    #print(a)
    b=a.to_frame(name="average_rates").reset_index()
    #b = px.data.gapminder()
    fig = px.line(b,x="checkin", y="average_rates", title='Rates in '+st+' stars hotels of '+c)

    htm = plotly.io.to_html(fig=fig, include_plotlyjs='cdn')
    f  = open('reder.html','w')
    f.write(htm)
    @app.route('/')
    def rungraph():
        return render_template('reder.html') 
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(host='127.0.0.1',port=5000)
