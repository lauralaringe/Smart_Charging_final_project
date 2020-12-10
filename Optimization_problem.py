# importing libraries 
import csv
import datetime
import re
import serial
import plotly.graph_objs as go
import pandas as pd

# import functions from other files
from Red_Electrica_Data import get_price_data
from RE_Data import get_irradiance_wind_data

price_df = get_price_data()
irradiance_df, wind_df = get_irradiance_wind_data()

current_hour = datetime.datetime.now().hour
end_hour = current_hour + 8 -1

price_to_check = price_df[current_hour:end_hour]

irradiance_to_check = irradiance_df[current_hour:end_hour]
wind_to_check = wind_df[current_hour:end_hour]
total_df = pd.DataFrame()
total_df['to_maximize'] = irradiance_to_check["G(h)"] + wind_to_check["WS10m"] - price_to_check[1]

# Get the 2 maximum
maximum1 = total_df['to_maximize'].nlargest(1)
maximum2 = total_df['to_maximize'].nlargest(2)


fig = go.Figure()

fig.add_trace(go.Scatter(x=price_df.index, y=price_df[1],
                    mode='lines',
                    name='price'))
fig.add_trace(go.Scatter(x=irradiance_df.index, y=irradiance_df["G(h)"],
                    mode='lines',
                    name='irradiance'))
fig.add_trace(go.Scatter(x=wind_df.index, y=wind_df["WS10m"],
                    mode='lines',
                    name='wind'))
fig.add_trace(go.Scatter(x=total_df.index, y=wind_df,
                    mode='lines',
                    name='total to optimize'))

fig.show()

#optimization problem:


