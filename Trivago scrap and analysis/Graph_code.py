import pandas as pd
import numpy as np
import plotly.express as px

#px.renderers.default = "browser"

def plot_graph(c,st,maxPrice):
    print(c)
    df=pd.read_csv("C:\\trivago_data\\"+c+st+"star"+".csv")
    #df=pd.read_csv(c+".csv")
    # maximum=int(input("Enter maximum rate : "))
    if(maxPrice != -1):
        df=df.drop(df[df['Rate'] > maxPrice].index)
    #print(df.describe())
    g=df.groupby(by='checkin')
    a=g['Rate'].agg(np.mean)
    #print(a)
    b=a.to_frame(name="average_rates").reset_index()
    #b = px.data.gapminder()
    fig = px.line(b,x="checkin", y="average_rates", title='Rates in '+st+' stars hotels of '+c)
    fig.show(renderer="browser")
