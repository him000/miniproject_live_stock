# miniproject_live_stock
Live stock price visualization

Visualization of live stock price data of different companies and it's comparison using DASH framework for python, 
Dash apps are composed of two parts. 
1.The first part is the "layout" of the app and it describes what the application looks like. 
2.The second part describes the interactivity of the application.
Dash generally provides Python classes for all of the visual components of the application. 
A set of components in the dash_core_components and the dash_html_components library.

Dash is a python framework for creating analytical web app
Dash is build on top of plotly.js, react and flask due to which dash has in-build  interactivity.
It supports reactive programming by providing dynamic changes in graph using app callbacks
Which can be attached to any input method like radiobuttons, text area etc. and output can be provided to a graph or any heading like html tag so that heading will change based on inputs.
All the graphs provided by plotly can be drawn on this .

This app uses nsetools() for python which provide live Nse market price of different companies and AlphaVantage is used to get historical data of the company.

Live data of 4 companies have been plotted and comparison between two companies is done based on closing market price of each month.  
Live graph changes at interval of 5 second which can be varying.
Historical data is of 24 months from current date.
 
