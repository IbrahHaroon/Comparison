import plotly.graph_objects as go 
import numpy as np 


def splitValues(value):
    splitValue = value / 2
    return splitValue

def plotter(x, y, z):
    # x1 = np.linspace(-abs(splitValues(x)), splitValues(x), 11) 
    # y1 = np.linspace(-abs(splitValues(y)), splitValues(y), 11) 
    # z1 = np.linspace(-abs(splitValues(z)), splitValues(z), 11) 

    x1 = np.linspace(-4, 0, 10) 
    y1 = np.linspace(-10, y, 10) 
    z1 = np.linspace(11, z, 10) 

    X, Y, Z = np.meshgrid(x1, y1, z1) 

    values = (np.sin(X**2 + Y**2))/(X**2 + Y**2) 

    fig = go.Figure(data=go.Volume( 
	x=X.flatten(), 
	y=Y.flatten(), 
	z=Z.flatten(), 
	value=values.flatten(), 
	opacity=1, 
	)) 

    fig.show()

plotter(10.0, 5.0, 2.0)