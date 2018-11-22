'''
import tkinter as tk
m=tk.Tk()
m.title("hello")
canvas=tk.Canvas(m,width=60,height=30)
canvas.pack()
button=tk.Button(m,text='Quit',command=m.destroy)
button.pack()

m.mainloop()

'''
'''
from nsetools import Nse
from pprint import pprint
import time
nse=Nse()
while(1):
	q=nse.get_quote('infy')
	pprint(q['lastPrice'])
	time.sleep(5)
'''

# -*- coding: utf-8 -*-
from nsetools import Nse
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py #to plot
import plotly.graph_objs as go # create object of different graphs
from dash.dependencies import Output, Event ,Input
from collections import deque
import requests
'''
x_axis_data=list(range(1,11))
y_axis_data=np.random.randn(10)+5
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Stock Price'),

    

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                #{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                go.Scatter(x=x_axis_data,y=y_axis_data,mode='lines+markers',name='plot2')
            		],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

'''
current='infosys'
nse=Nse()
compare=0
X_info = deque(maxlen=500)
X_info.append(1)
Y_info = deque(maxlen=500)
Y_info.append(nse.get_quote('infy')['lastPrice'])

X_reli = deque(maxlen=500)
X_reli.append(1)
Y_reli = deque(maxlen=500)
Y_reli.append(nse.get_quote('reliance')['lastPrice'])

X_wipro = deque(maxlen=500)
X_wipro.append(1)
Y_wipro = deque(maxlen=500)
Y_wipro.append(nse.get_quote('wipro')['lastPrice'])

X_itc = deque(maxlen=500)
X_itc.append(1)
Y_itc = deque(maxlen=500)
Y_itc.append(nse.get_quote('itc')['lastPrice'])



data={} 
r=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=54DOWF27U8Y1LQ1B')
data=dict(r.json())
data=data['Monthly Time Series']
date1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
points=list(data.values())
new_points1=[]
for i in range(0,24) :
    new_points1.append(np.float64(points[i]['4. close']))
new_points1.reverse()
data={} 
r=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=54DOWF27U8Y1LQ1B')
data=dict(r.json())
data=data['Monthly Time Series']
date2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
points=list(data.values())
new_points2=[]
for i in range(0,24) :
    new_points2.append(np.float64(points[i]['4. close']))
new_points2.reverse()
him_data1=go.Scatter(x=list(date1),y=list(new_points1), name='Microsoft',mode= 'lines')
him_data2=go.Scatter(x=list(date2),y=list(new_points2), name='Apple',mode= 'lines')




#html.p() is placeholder to manage callback withput output 

#interval is in millisecond
#dcc.interval generate an event every 1 sec and app.callback fire based on it
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1("STOCK PRICE",style={'textAlign' : 'center','color' : '#7FDBFF' }),
        html.H3(id='him'),
        html.P(id='waste'),
        dcc.Graph(id='live-graph', animate=True),  html.Div(dcc.Graph(id='hello')),

        dcc.RadioItems(
                id='radio',
                options=[{'label': i, 'value': i} for i in ['infosys', 'reliance','wipro','itc','compare']],
                value='infosys',
                labelStyle={'display': 'inline-block','margin':'5px'}
            ),

        dcc.Interval(
            id='graph-update',
            interval=1*5000 
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    q=nse.get_quote('infy')
    if(len(X_info)==488):
        X_info.popleft()
        Y_info.popleft()    

    X_info.append(X_info[-1]+1)
    Y_info.append(q['lastPrice'])

    data1 = go.Scatter(
            x=list(X_info),
            y=list(Y_info),
            name='Line',
            mode= 'lines',
            line= dict(color = 'rgb(12, 100, 24)')
            )

    
    q=nse.get_quote('reliance')
    if(len(X_reli)==488):
        X_reli.popleft()
        Y_reli.popleft()    

    X_reli.append(X_reli[-1]+1)
    Y_reli.append(q['lastPrice'])

    data2 = go.Scatter(
            x=list(X_reli),
            y=list(Y_reli),
            name='Line',
            mode= 'lines',
            line= dict(color = 'rgb(128, 230, 24)')
            )

    q=nse.get_quote('wipro')
    if(len(X_wipro)==488):
        X_wipro.popleft()
        Y_wipro.popleft()    

    X_wipro.append(X_wipro[-1]+1)
    Y_wipro.append(q['lastPrice'])

    data3 = go.Scatter(
            x=list(X_wipro),
            y=list(Y_wipro),
            name='Line',
            mode= 'lines',
            line= dict(color = 'rgb(12, 100, 142)')
            )

    q=nse.get_quote('itc')
    if(len(X_wipro)==488):
        X_itc.popleft()
        Y_itc.popleft()    

    X_itc.append(X_itc[-1]+1)
    Y_itc.append(q['lastPrice'])

    data4 = go.Scatter(
            x=list(X_itc),
            y=list(Y_itc),
            name='Line',
            mode= 'lines',
            line =dict(color = ('rgb(205, 12, 24)'))
            )
    if(compare==1):
    	him=history()
    	return{'data':[him]}
    else :
    	if current=='infosys':
    		return {'data': [data1],'layout' : go.Layout(xaxis=dict(range=[min(X_info),max(X_info)],title="Interval(4-Second)"),
	                                                yaxis=dict(range=[min(Y_info)-0.8,max(Y_info)+0.8],title="Price"),
	                                                )}
    	elif current=='reliance':
    		return {'data': [data2],'layout' : go.Layout(xaxis=dict(range=[min(X_reli),max(X_reli)],title="Interval(4-Second)"),
	                                                yaxis=dict(range=[min(Y_reli)-0.8,max(Y_reli)+0.8],title="Price"),
	                                                )}
    	elif current=='wipro':
    		return {'data': [data3],'layout' : go.Layout(xaxis=dict(range=[min(X_wipro),max(X_wipro)],title="Interval(4-Second)"),
	                                            yaxis=dict(range=[min(Y_wipro)-0.8,max(Y_wipro)+0.8],title="Price"),
	                                            )}
    	elif current=='itc':
    		return {'data': [data4],'layout' : go.Layout(xaxis=dict(range=[min(X_itc),max(X_itc)],title="Interval(4-Second)"),
	                                            yaxis=dict(range=[min(Y_itc)-0.8,max(Y_itc)+0.8],title="Price"),
	                                            )}




@app.callback(Output('him','children'),
              [Input('radio', 'value')])
def update(radio_value):
	global compare
	global current
	print(current)
	if radio_value == "infosys" :
	    current="infosys"
	elif radio_value == "reliance":
	    current="reliance"
	elif radio_value == "wipro":
	    current="wipro"
	elif radio_value == "itc":
	    current="itc"
	return current.upper()


@app.callback(Output('hello','figure'),
				[Input('radio','value')])
def update_value(radio_value):
	global him_data1,him_data2
	if radio_value == 'compare' :
		return{'data':[him_data1,him_data2],'layout':go.Layout(xaxis=dict(title="Months"),
	                                            yaxis=dict(title="Stock Price"),
	                                            )}



	
if __name__ == '__main__':
    app.run_server(debug=True)
