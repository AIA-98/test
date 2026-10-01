from feature_functions import *
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly import tools

df = pd.read_csv('EURUSD_Hourly.csv')

# Rename the columns for easier access
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

# Convert the date column to datetime format
df.date = pd.to_datetime(df.date, format='%d.%m.%Y %H:%M:%S.%f')

# Set the date column as the index of the DataFrame
df = df.set_index(df.date)

# Keep only the open, high, low, close, and volume columns
df = df[['open', 'high', 'low', 'close', 'volume']]

# Remove duplicate indices
df = df.drop_duplicates(keep='last')

# Calculate the moving average for the close prices with a 30-hour window
ma = df.close.rolling(center=False, window=30).mean()

##part (2) - get function data from selected function:
HAresults= heikin_ashi(df,[1])
HA = HAresults.candles[1]

#plot!
# Create OHLC and volume traces for plotting
trace0 = go.Ohlc(x=df.index, open=df.open, high=df.high, low=df.low, close=df.close, name='Currency Quote')
trace1 = go.Scatter(x=df.index, y=ma)
trace2 = go.Ohlc(x=HA.index, open=HA.open, high=HA.high, low=HA.low, close=HA.close, name='Heikin Ashi')


# Combine the traces
data = [trace0, trace1, trace2]

# Create a figure with subplots
fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)

# Add traces to the figure
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

# Plot the figure and save it as an HTML file
pyo.plot(fig, filename='tutorial.html')

