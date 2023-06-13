##Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from math import pi
import statistics
import string
import altair as alt




st.title("Tracer Study")

# Function for bar chart visualization
def visualize_bar_chart(data):
    colorresp = ['steelblue', 'orange', 'yellowgreen', 'mediumpurple', 'indianred']
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Percentage:Q', scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(title='Percentage')),
        color=alt.Color('Year:N', legend=None, scale=alt.Scale(range=colorresp)),
        tooltip=['Year', 'Percentage']
    )
    st.altair_chart(chart, use_container_width=True)
    
def visualize_line_chart(data):
    colorresp = ['steelblue', 'orange', 'yellowgreen', 'mediumpurple', 'indianred']
    chart = alt.Chart(data).mark_line().encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('Percentage:Q', scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(title='Percentage')),
        color=alt.Color('Year:N', legend=None, scale=alt.Scale(range=colorresp)),
        tooltip=['Year', 'Percentage']
    )
    st.altair_chart(chart, use_container_width=True)



# Specify the path of the file
path2 = "C:/Users/MSI/Downloads/Magang Tracer Study Script/Data responden 2018-2022.xlsx"

# Create an empty DataFrame to store the grouped data
data_frames = []

# Loop through each year
for year in range(2018, 2023):
    if year >= 2018 and year <= 2020:
        sheet_name = f'sarjana_{year}_ ang.{year-7}'
    else:
        sheet_name = f'sarjana_{year}_ang.{year-7}'

    try:
        # Read the Excel sheet for the current year
        df = pd.read_excel(path2, sheet_name=sheet_name, header=0)

        # Filter the dataframe to include only the columns 'PRODI', 'Fakultas', and '%'
        filtered_data = df[['PRODI', 'Fakultas', '%']]

        # Multiply the '%' column by 100
        filtered_data['%'] = filtered_data['%'] * 100

        # Add the year column to the filtered data
        filtered_data['Year'] = year

        # Rename the '%' column to 'Percentage'
        filtered_data = filtered_data.rename(columns={'%': 'Percentage'})

        # Append the filtered data to the list of data frames
        data_frames.append(filtered_data)

    except FileNotFoundError:
        # Handle the case when the sheet is not found
        # Create a DataFrame with 0 values for the missing year
        missing_data = pd.DataFrame({
            'PRODI': '',
            'Fakultas': '',
            'Percentage': 0,
            'Year': year
        }, index=[0])

        # Append the missing data to the list of data frames
        data_frames.append(missing_data)

# Concatenate all the data frames into a single DataFrame
data_df = pd.concat(data_frames, ignore_index=True)

# Sort the DataFrame by 'Year' and 'PRODI'
data_df = data_df.sort_values(['Year', 'PRODI'])

# Create a list of unique program names
programs = data_df['PRODI'].unique()

# Select the Fakultas
# selected_fakultas = st.selectbox('Select Fakultas:',+ list(data_df['Fakultas'].unique()), index=0)
# Select the Fakultas
selected_fakultas = st.selectbox('Select Fakultas:', data_df['Fakultas'].unique(), index=10)
# Filter the data based on the selected Fakultas
filtered_data = data_df[data_df['Fakultas'] == selected_fakultas]

# Select the PRODI based on the chosen Fakultas
selected_prodi = st.selectbox('Select Program Studi:', filtered_data['PRODI'].unique())

# Filter the data further based on the selected PRODI
program_data = filtered_data[filtered_data['PRODI'] == selected_prodi]

# Select the visualization options
visualization_options = st.multiselect('Select Visualization:', ['Bar Chart Responden', 'Line Chart'])
st.write("##")
st.write("##")
st.write("##")
st.write("##")
# Visualize the data if visualization options are selected
if visualization_options:
    for option in visualization_options:
        if option == 'Bar Chart Responden':
            visualize_bar_chart(program_data)
        elif option == 'Line Chart':
            visualize_line_chart(program_data)
        # Add more visualization options and corresponding functions as needed

